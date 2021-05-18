# Copyright 2021 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Model builder.

The model builder let the user create models by hand i.e. by defining the tree
structure manually.

The available builders are:

  - RandomForestBuilder
  - CARTBuilder
  - GradientBoostedTreeBuilder

Usage:

```python

# Create a binary classification CART model.
builder = builder_lib.CARTBuilder(
  path="/path/to/model",
  objective=py_tree.objective.ClassificationObjective(
  label="color", classes=["red", "blue"]))

# Create the tree
#  f1>=1.5
#    ├─(pos)─ [0.1, 0.9]
#    └─(neg)─ [0.8, 0.2]
#
# The component of the trees (e.g. `NonLeafNode`, `Tree`) are defined in
# `tfdf.py_tree.`.
#
builder.add_tree(
    Tree(
        NonLeafNode(
            condition=NumericalHigherThanCondition(
                feature=SimpleColumnSpec(
                    name="f1", type=py_tree.dataspec.ColumnType.NUMERICAL),
                threshold=1.5,
                missing_evaluation=False),
            pos_child=LeafNode(
                value=ProbabilityValue(probability=[0.1, 0.9])),
            neg_child=LeafNode(
                value=ProbabilityValue(probability=[0.8, 0.2])))))

builder.close()

# Load and use the model
model = tf.keras.models.load_model("/path/to/model")
predictions = model.predict(...)
```
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
from enum import Enum  # pylint: disable=g-importing-member
import os
from typing import List, Any, Optional, Dict, Tuple, Union

import six
import tensorflow as tf

from tensorflow_decision_forests.component import py_tree
from tensorflow_decision_forests.component.inspector import blob_sequence
from tensorflow_decision_forests.component.inspector import inspector as inspector_lib
from tensorflow_decision_forests.keras import core as keras_core
from yggdrasil_decision_forests.dataset import data_spec_pb2
from yggdrasil_decision_forests.model import abstract_model_pb2
from yggdrasil_decision_forests.model.gradient_boosted_trees import gradient_boosted_trees_pb2
from yggdrasil_decision_forests.model.random_forest import random_forest_pb2

Task = abstract_model_pb2.Task
ColumnType = data_spec_pb2.ColumnType


class ModelFormat(Enum):
  """Model formats on disk."""

  # TensorFlow SavedModel format.
  # Note: This format contains an Yggdrasil model in the "assets" sub-directory.
  TENSORFLOW_SAVED_MODEL = 1

  # Yggdrasil Decision Forest format.
  YGGDRASIL_DECISION_FOREST = 2


@six.add_metaclass(abc.ABCMeta)
class AbstractBuilder(object):
  """Generic model builder."""

  def __init__(self, path: str, objective: py_tree.objective.AbstractObjective,
               model_format: Optional[ModelFormat]):

    if not path:
      raise ValueError("The path cannot be empty")

    self._path = path
    self._objective = objective
    self._model_format = model_format
    self._header = abstract_model_pb2.AbstractModel()
    self._dataspec = data_spec_pb2.DataSpecification()
    self._closed = False

    self._header.name = self.model_type()
    self._header.task = objective.task

    # Index of the column indices in `_dataspec` by name.
    self._dataspec_column_index: Dict[str, int] = {}

    self._initialize_header_column_idx()

    tf.io.gfile.makedirs(self.yggdrasil_model_path())

  def close(self):
    """Finalize the builder work.

    This method should be called last.
    """

    if self._closed:
      raise ValueError("Model builder already closed")
    self._closed = True

    # List the input features.
    #
    # The first two column indices are used by the label and the ranking (if
    # this is a ranking problem).
    first_feature_idx = 1
    if self._header.task == Task.RANKING:
      first_feature_idx = 2
    self._header.input_features[:] = range(first_feature_idx,
                                           len(self._dataspec.columns))

    # Write the model header.
    _write_binary_proto(
        self._header,
        os.path.join(self.yggdrasil_model_path(),
                     inspector_lib.FILENAME_HEADER))

    # Write the dataspec.
    _write_binary_proto(
        self._dataspec,
        os.path.join(self.yggdrasil_model_path(),
                     inspector_lib.FILENAME_DATASPEC))

    # Write the "done" file.
    #
    # A model is considered invalid without it.
    with tf.io.gfile.GFile(
        os.path.join(self.yggdrasil_model_path(), inspector_lib.FILENAME_DONE),
        "wb") as f:
      f.write("done")

    if self._model_format == ModelFormat.TENSORFLOW_SAVED_MODEL:
      # Wrap the Yggdrasil model into a tensorflow Saved Model.
      keras_core.yggdrasil_model_to_keras_model(self.yggdrasil_model_path(),
                                                self._path)
      tf.io.gfile.rmtree(self.yggdrasil_model_path())

  def yggdrasil_model_path(self):
    """Gets the path to the destination yggdrasil model."""

    if self._model_format == ModelFormat.TENSORFLOW_SAVED_MODEL:
      return os.path.join(self._path, "tmp")

    elif self._model_format == ModelFormat.YGGDRASIL_DECISION_FOREST:
      return self._path

    else:
      raise NotImplementedError()

  @abc.abstractmethod
  def model_type(self) -> str:
    """Unique key describing the type of the model."""

    raise NotImplementedError()

  @property
  def dataspec(self) -> data_spec_pb2.DataSpecification:
    """Dataspec, possibly partially constructed.

    Can be called before `close` for advanced model edition.
    """

    return self._dataspec

  @property
  def objective(self) -> py_tree.objective.AbstractObjective:
    """Objective of the model."""

    return self._objective

  def observe_feature(self,
                      feature: inspector_lib.SimpleColumnSpec,
                      categorical_values: Optional[Union[List[str],
                                                         List[int]]] = None):
    """Register a feature and some of its possible value.

    Generally, users don't need to call this function. An example of advanced
    exception is if a model does not refer to a specific possible categorical
    value, and if this value should be threader differently that the
    Out-of-vocabulary.

    Should be called at least once on each of the model input features.
    If called multiple times with `categorical_values` the set of possible
    values will be the union of the `categorical_values`s.

    Args:
      feature: Definition of the feature.
      categorical_values: Set of observed values. Only for categorical-like
        features.
    """

    # Register the name.
    col_idx, created = self._get_or_create_column_idx(feature.name)

    # Register the type.
    if feature.type != ColumnType.UNKNOWN:
      existing_type = self._dataspec.columns[col_idx].type
      if (existing_type != ColumnType.UNKNOWN and
          feature.type != existing_type):
        raise ValueError("Inconstant feature type for "
                         f"{feature.name}: {feature.type} vs {existing_type}")
      self._dataspec.columns[col_idx].type = feature.type

    # Register the values.
    # Currently, only the categorical values are registered.
    column = self._dataspec.columns[col_idx]
    if categorical_values and column.type in [
        ColumnType.CATEGORICAL, ColumnType.CATEGORICAL_SET
    ]:
      is_already_integerized = isinstance(categorical_values[0], int)
      if is_already_integerized:
        # The value is stored as a dense integer.
        column.categorical.number_of_unique_values = max(
            column.categorical.number_of_unique_values,
            max(categorical_values) + 1)
      else:
        # The value is stored as a string.
        if created:
          # Create the out-of-vocabulary item.
          column.categorical.items["<OOV>"].index = 0
          column.categorical.number_of_unique_values = 1
        for value in categorical_values:
          if value not in column.categorical.items:
            column.categorical.items[value].index = len(
                column.categorical.items)
            column.categorical.number_of_unique_values = len(
                column.categorical.items)

  def _get_or_create_column_idx(self, col_name: str) -> Tuple[int, bool]:
    """Returns the index of the column with a given name.

    Creates the column if it does not exist.

    Args:
      col_name: Name of the columns.

    Returns:
      Index of the column, and whether the column was just created.
    """

    index = self._dataspec_column_index.get(col_name)
    if index is not None:
      return index, False

    # The column does not exist.
    index = len(self._dataspec.columns)
    column = self._dataspec.columns.add()
    column.name = col_name
    self._dataspec_column_index[col_name] = index
    return index, True

  def _initialize_header_column_idx(self):
    """Sets the column idx fields in the header.

    Should be called once before writing the header to disk.
    """

    # The first column is the label.
    self._header.label_col_idx = 0
    label_column = self._dataspec.columns.add()
    label_column.name = self._objective.label
    if isinstance(self._objective, py_tree.objective.ClassificationObjective):
      label_column.type = ColumnType.CATEGORICAL

      # One value is reserved for the non-used OOV item.
      label_column.categorical.number_of_unique_values = self._objective.num_classes + 1

      if not self._objective.has_integer_labels:
        label_column.categorical.items["<OOV>"].index = 0
        for idx, value in enumerate(self._objective.classes):
          label_column.categorical.items[value].index = idx + 1
        assert len(label_column.categorical.items
                  ) == label_column.categorical.number_of_unique_values

    elif isinstance(self._objective, (py_tree.objective.RegressionObjective,
                                      py_tree.objective.RankingObjective)):
      label_column.type = ColumnType.NUMERICAL

    else:
      raise NotImplementedError(f"No supported objective {self._objective}")

    if isinstance(self._objective, py_tree.objective.RankingObjective):
      # Create the "group" column for Ranking.
      self._header.ranking_group_col_idx = 1
      group_column = self._dataspec.columns.add()
      group_column.type = ColumnType.HASH
      group_column.name = self._objective.group


@six.add_metaclass(abc.ABCMeta)
class AbstractDecisionForestBuilder(AbstractBuilder):
  """Generic decision forest model builder."""

  def __init__(self, path: str, objective: py_tree.objective.AbstractObjective,
               model_format: Optional[ModelFormat]):

    super(AbstractDecisionForestBuilder, self).__init__(path, objective,
                                                        model_format)

    num_node_shards = 1  # Store all the nodes in a single shard.
    self.specialized_header().num_node_shards = num_node_shards
    self.specialized_header().node_format = "BLOB_SEQUENCE"
    self._node_writer = blob_sequence.Writer(
        os.path.join(
            self.yggdrasil_model_path(),
            "{}-{:05d}-of-{:05d}".format(inspector_lib.FILENAME_NODES_SHARD, 0,
                                         num_node_shards)))

  def close(self):

    # Write the model specialized header.
    _write_binary_proto(
        self.specialized_header(),
        os.path.join(self.yggdrasil_model_path(),
                     self.specialized_header_filename()))

    # Close the output node stream.
    self._node_writer.close()
    self._node_writer = None

    # Should be called last.
    super(AbstractDecisionForestBuilder, self).close()

  @abc.abstractmethod
  def specialized_header(self) -> Any:
    """Gets the specialized header of the model."""

    raise NotImplementedError()

  @abc.abstractmethod
  def specialized_header_filename(self) -> str:
    """Gets the filename of the specialized header."""

    raise NotImplementedError()

  def add_tree(self, tree: py_tree.tree.Tree):
    """Adds one tree to the model."""

    self._write_branch(tree.root)
    self.specialized_header().num_trees += 1

  def check_leaf(self, node: py_tree.node.LeafNode):
    """Called on all the leaf nodes during the export."""

    pass

  def check_non_leaf(self, node: py_tree.node.NonLeafNode):
    """Called on all the non-leaf nodes during the export."""

    pass

  def _write_branch(self, node: py_tree.node.AbstractNode):
    """Write of a node and its children to the writer.

    Nodes are written in a Depth First Pre-order traversals (as expected by the
    model format).

    This function is the inverse of inspector_lib._extract_branch.

    Args:
      node: The node to write.
    """

    # Possibly register the feature.
    if isinstance(node, py_tree.node.NonLeafNode):
      self.check_non_leaf(node)
      if isinstance(node.condition,
                    (py_tree.condition.CategoricalIsInCondition,
                     py_tree.condition.CategoricalSetContainsCondition)):
        self.observe_feature(node.condition.feature, node.condition.mask)
      else:
        for feature in node.condition.features():
          self.observe_feature(feature)
    elif isinstance(node, py_tree.node.LeafNode):
      self.check_leaf(node)

    # Converts the node into a proto node.
    core_node = py_tree.node.node_to_core_node(node, self.dataspec)

    # Write the node to disk.
    self._node_writer.write(core_node.SerializeToString())

    # Recursive call on the children.
    if isinstance(node, py_tree.node.NonLeafNode):
      self._write_branch(node.neg_child)
      self._write_branch(node.pos_child)


class RandomForestBuilder(AbstractDecisionForestBuilder):
  """Random Forest model builder."""

  def __init__(
      self,
      path: str,
      objective: py_tree.objective.AbstractObjective,
      model_format: Optional[ModelFormat] = ModelFormat.TENSORFLOW_SAVED_MODEL,
      winner_take_all: Optional[bool] = False):
    self._specialized_header = random_forest_pb2.Header(
        winner_take_all_inference=winner_take_all)

    # Should be called last.
    super(RandomForestBuilder, self).__init__(path, objective, model_format)

  def model_type(self) -> str:
    return "RANDOM_FOREST"

  def specialized_header(self) -> Any:
    return self._specialized_header

  def specialized_header_filename(self) -> str:
    return "random_forest_header.pb"

  def check_leaf(self, node: py_tree.node.LeafNode):

    if isinstance(self.objective, py_tree.objective.ClassificationObjective):
      if not isinstance(node.value, py_tree.value.ProbabilityValue):
        raise ValueError("A classification objective requires leaf nodes"
                         " with classification values.")

      if len(node.value.probability) != self.objective.num_classes:
        raise ValueError(
            "The number of dimensions of the probability of "
            "the classification value ({len(node.value.probability)}) does not "
            "match the number of classes of the label in the objective "
            "({self.objective.num_classes})")

    elif isinstance(self.objective, py_tree.objective.RegressionObjective):
      if not isinstance(node.value, py_tree.value.RegressionValue):
        raise ValueError("A regression objective requires leaf nodes"
                         " with regressive values.")

    elif isinstance(self.objective, py_tree.objective.RankingObjective):
      raise ValueError("Ranking objective not supported by this model")

    else:
      raise NotImplementedError()


class CARTBuilder(RandomForestBuilder):
  """CART model builder.

  A CART is represented as a Random Forest with one tree.
  """

  def add_tree(self, tree: py_tree.tree.Tree):

    if self.specialized_header().num_trees > 0:
      raise ValueError(
          "A CART only has one tree. Use a Random Forest (or another "
          "decision forest model) to create models with multiple trees.")

    super(CARTBuilder, self).add_tree(tree)


class GradientBoostedTreeBuilder(AbstractDecisionForestBuilder):
  """Gradient Boosted Tree model builder."""

  def __init__(
      self,
      path: str,
      objective: py_tree.objective.AbstractObjective,
      bias: Optional[float] = 0.0,
      model_format: Optional[ModelFormat] = ModelFormat.TENSORFLOW_SAVED_MODEL):

    # Compute the number of tree per iterations and loss.
    #
    # The loss defines the activation function applied on the logits.
    if isinstance(objective, py_tree.objective.ClassificationObjective):

      if objective.num_classes == 2:
        # Binary classification
        num_trees_per_iter = 1
        loss = gradient_boosted_trees_pb2.Loss.BINOMIAL_LOG_LIKELIHOOD
        bias = [bias]

      else:
        # Multi class classification
        num_trees_per_iter = objective.num_classes
        loss = gradient_boosted_trees_pb2.Loss.MULTINOMIAL_LOG_LIKELIHOOD
        if bias != 0.0:
          raise ValueError(
              "The bias should be zero for multi-class classification")
        bias = [bias] * num_trees_per_iter

    elif isinstance(objective, py_tree.objective.RegressionObjective):
      num_trees_per_iter = 1
      loss = gradient_boosted_trees_pb2.Loss.SQUARED_ERROR
      bias = [bias]

    elif isinstance(objective, py_tree.objective.RankingObjective):
      num_trees_per_iter = 1
      loss = gradient_boosted_trees_pb2.Loss.LAMBDA_MART_NDCG5
      bias = [bias]

    else:
      raise NotImplementedError()

    # Check the bias shape.
    if len(bias) != num_trees_per_iter:
      raise ValueError(
          f"The objective expects a bias of dimension {num_trees_per_iter}")

    self._specialized_header = gradient_boosted_trees_pb2.Header(
        initial_predictions=bias,
        num_trees_per_iter=num_trees_per_iter,
        loss=loss)

    # Should be called last.
    super(GradientBoostedTreeBuilder, self).__init__(path, objective,
                                                     model_format)

  def model_type(self) -> str:
    return "GRADIENT_BOOSTED_TREES"

  def close(self):

    if (self._specialized_header.num_trees %
        self._specialized_header.num_trees_per_iter) != 0:
      raise ValueError(
          "The model should have number of trees which is "
          "a multiple of the output-size i.e. bias-size. "
          f"{self._specialized_header.num_trees} is not a "
          f"multiple of {self._specialized_header.num_trees_per_iter}.")

    # Should be called last.
    super(GradientBoostedTreeBuilder, self).close()

  def specialized_header(self) -> Any:
    return self._specialized_header

  def specialized_header_filename(self) -> str:
    return "gradient_boosted_trees_header.pb"

  def check_leaf(self, node: py_tree.node.LeafNode):
    if not isinstance(node.value, py_tree.value.RegressionValue):
      raise ValueError("A GBT model should only have leaf with regressive "
                       f"value. Got {node.value} instead.")


def _write_binary_proto(proto: Any, path: str):
  """Writes a binary serialized proto from disk."""

  with tf.io.gfile.GFile(path, "wb") as f:
    f.write(proto.SerializeToString())
