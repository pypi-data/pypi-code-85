"""BalancedRandomForestClassifier: Forest classifiers trained 
on balanced boostrasp samples."""

# Authors: Zhining Liu <zhining.liu@outlook.com>
#          Guillaume Lemaitre <g.lemaitre58@gmail.com>
# License: MIT

# %%


import numbers
from warnings import warn
from copy import deepcopy

import numpy as np
from numpy import float32 as DTYPE
from numpy import float64 as DOUBLE
from scipy.sparse import issparse
from collections import Counter

from joblib import Parallel, delayed

from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble._base import _set_random_states
from sklearn.ensemble._forest import (_get_n_samples_bootstrap,
                                      _parallel_build_trees,
                                      _generate_unsampled_indices,)
from sklearn.exceptions import DataConversionWarning
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import check_array, check_random_state, _safe_indexing
from sklearn.utils.validation import _check_sample_weight


from ..base import ImbalancedEnsembleClassifierMixin, MAX_INT
from ...sampler.under_sampling import RandomUnderSampler
from ...pipeline import make_pipeline
from ...utils._validation_data import check_eval_datasets
from ...utils._validation_param import (check_train_verbose, 
                                        check_eval_metrics)
from ...utils._validation import (_deprecate_positional_args,
                                  check_sampling_strategy)
from ...utils._docstring import (Substitution, FuncSubstitution, 
                                 FuncGlossarySubstitution,
                                 _get_parameter_docstring, 
                                 _get_example_docstring)

# # For local test
# import sys
# sys.path.append("../..")
# from ensemble.base import ImbalancedEnsembleClassifierMixin, MAX_INT
# from sampler.under_sampling import RandomUnderSampler
# from pipeline import make_pipeline
# from utils._validation_data import check_eval_datasets
# from utils._validation_param import (check_train_verbose, 
#                                      check_eval_metrics)
# from utils._validation import (_deprecate_positional_args,
#                                check_sampling_strategy)
# from utils._docstring import (Substitution, FuncSubstitution, 
#                               _get_parameter_docstring, 
#                               _get_example_docstring)


# Properties
_method_name = 'BalancedRandomForestClassifier'
_sampler_class = RandomUnderSampler

_solution_type = 'resampling'
_sampling_type = 'under-sampling'
_ensemble_type = 'random-forest'
_training_type = 'parallel'

_properties = {
    'sampling_type': _sampling_type,
    'solution_type': _solution_type,
    'ensemble_type': _ensemble_type,
    'training_type': _training_type,
}

_super = RandomForestClassifier

def _local_parallel_build_trees(
    sampler,
    tree,
    forest,
    X,
    y,
    sample_weight,
    tree_idx,
    n_trees,
    verbose=0,
    class_weight=None,
    n_samples_bootstrap=None,
):
    # resample before to fit the tree
    X_resampled, y_resampled = sampler.fit_resample(X, y)
    if sample_weight is not None:
        sample_weight = _safe_indexing(sample_weight, sampler.sample_indices_)
    if _get_n_samples_bootstrap is not None:
        n_samples_bootstrap = min(n_samples_bootstrap, X_resampled.shape[0])
    tree = _parallel_build_trees(
        tree,
        forest,
        X_resampled,
        y_resampled,
        sample_weight,
        tree_idx,
        n_trees,
        verbose=verbose,
        class_weight=class_weight,
        n_samples_bootstrap=n_samples_bootstrap,
    )
    return sampler, tree, y_resampled.shape[0]


@Substitution(
    random_state=_get_parameter_docstring('random_state', **_properties),
    n_jobs=_get_parameter_docstring('n_jobs', **_properties),
    example=_get_example_docstring(_method_name)
)
class BalancedRandomForestClassifier(ImbalancedEnsembleClassifierMixin,
                                     RandomForestClassifier):
    """A balanced random forest classifier.

    A balanced random forest randomly under-samples each boostrap sample to
    balance it.

    Parameters
    ----------
    n_estimators : int, default=100
        The number of trees in the forest.

    criterion : {{"gini", "entropy"}}, default="gini"
        The function to measure the quality of a split. Supported criteria are
        "gini" for the Gini impurity and "entropy" for the information gain.
        Note: this parameter is tree-specific.

    max_depth : int, default=None
        The maximum depth of the tree. If None, then nodes are expanded until
        all leaves are pure or until all leaves contain less than
        min_samples_split samples.

    min_samples_split : int or float, default=2
        The minimum number of samples required to split an internal node:

        - If int, then consider `min_samples_split` as the minimum number.
        - If float, then `min_samples_split` is a percentage and
          `ceil(min_samples_split * n_samples)` are the minimum
          number of samples for each split.

    min_samples_leaf : int or float, default=1
        The minimum number of samples required to be at a leaf node:

        - If int, then consider ``min_samples_leaf`` as the minimum number.
        - If float, then ``min_samples_leaf`` is a fraction and
          `ceil(min_samples_leaf * n_samples)` are the minimum
          number of samples for each node.

    min_weight_fraction_leaf : float, default=0.0
        The minimum weighted fraction of the sum total of weights (of all
        the input samples) required to be at a leaf node. Samples have
        equal weight when sample_weight is not provided.

    max_features : {{"auto", "sqrt", "log2"}}, int, float, or None, default="auto"
        The number of features to consider when looking for the best split:

        - If int, then consider `max_features` features at each split.
        - If float, then `max_features` is a percentage and
          `int(max_features * n_features)` features are considered at each
          split.
        - If "auto", then `max_features=sqrt(n_features)`.
        - If "sqrt", then `max_features=sqrt(n_features)` (same as "auto").
        - If "log2", then `max_features=log2(n_features)`.
        - If None, then `max_features=n_features`.

        Note: the search for a split does not stop until at least one
        valid partition of the node samples is found, even if it requires to
        effectively inspect more than ``max_features`` features.

    max_leaf_nodes : int, default=None
        Grow trees with ``max_leaf_nodes`` in best-first fashion.
        Best nodes are defined as relative reduction in impurity.
        If None then unlimited number of leaf nodes.

    min_impurity_decrease : float, default=0.0
        A node will be split if this split induces a decrease of the impurity
        greater than or equal to this value.
        The weighted impurity decrease equation is the following::

            N_t / N * (impurity - N_t_R / N_t * right_impurity
                                - N_t_L / N_t * left_impurity)

        where ``N`` is the total number of samples, ``N_t`` is the number of
        samples at the current node, ``N_t_L`` is the number of samples in the
        left child, and ``N_t_R`` is the number of samples in the right child.
        ``N``, ``N_t``, ``N_t_R`` and ``N_t_L`` all refer to the weighted sum,
        if ``sample_weight`` is passed.

    bootstrap : bool, default=True
        Whether bootstrap samples are used when building trees.

    oob_score : bool, default=False
        Whether to use out-of-bag samples to estimate
        the generalization accuracy.

    replacement : bool, default=False
        Whether or not to sample randomly with replacement or not.

    {n_jobs}

    {random_state}

    verbose : int, default=0
        Controls the verbosity of the tree building process.

    warm_start : bool, default=False
        When set to ``True``, reuse the solution of the previous call to fit
        and add more estimators to the ensemble, otherwise, just fit a whole
        new forest.

    class_weight : dict, list of dicts, {{"balanced", "balanced_subsample"}}, default=None
        Weights associated with classes in the form dictionary with the key
        being the class_label and the value the weight.
        If not given, all classes are supposed to have weight one. For
        multi-output problems, a list of dicts can be provided in the same
        order as the columns of y.
        Note that for multioutput (including multilabel) weights should be
        defined for each class of every column in its own dict. For example,
        for four-class multilabel classification weights should be
        [{{0: 1, 1: 1}}, {{0: 1, 1: 5}}, {{0: 1, 1: 1}}, {{0: 1, 1: 1}}]
        instead of [{{1:1}}, {{2:5}}, {{3:1}}, {{4:1}}].
        The "balanced" mode uses the values of y to automatically adjust
        weights inversely proportional to class frequencies in the input data
        as ``n_samples / (n_classes * np.bincount(y))``
        The "balanced_subsample" mode is the same as "balanced" except that
        weights are computed based on the bootstrap sample for every tree
        grown.
        For multi-output, the weights of each column of y will be multiplied.
        Note that these weights will be multiplied with sample_weight (passed
        through the fit method) if sample_weight is specified.

    ccp_alpha : non-negative float, default=0.0
        Complexity parameter used for Minimal Cost-Complexity Pruning. The
        subtree with the largest cost complexity that is smaller than
        ``ccp_alpha`` will be chosen. By default, no pruning is performed.

    max_samples : int or float, default=None
        If bootstrap is True, the number of samples to draw from X
        to train each base estimator.

            - If ``None`` (default), then draw `X.shape[0]` samples.
            - If ``int``, then draw `max_samples` samples.
            - If ``float``, then draw `max_samples * X.shape[0]` samples. Thus,
              `max_samples` should be in the interval `(0, 1)`.

        Be aware that the final number samples used will be the minimum between
        the number of samples given in `max_samples` and the number of samples
        obtained after resampling.

    Attributes
    ----------
    estimators_ : list of DecisionTreeClassifier
        The collection of fitted sub-estimators.

    samplers_ : list of RandomUnderSampler
        The collection of fitted samplers.
    
    estimators_n_training_samples_ : list of ints
        The number of training samples for each fitted 
        base estimators.

    pipelines_ : list of Pipeline.
        The collection of fitted pipelines (samplers + trees).

    classes_ : ndarray of shape (n_classes,) or a list of such arrays
        The classes labels (single output problem), or a list of arrays of
        class labels (multi-output problem).

    n_classes_ : int or list
        The number of classes (single output problem), or a list containing the
        number of classes for each output (multi-output problem).

    n_features_ : int
        The number of features when ``fit`` is performed.

    n_outputs_ : int
        The number of outputs when ``fit`` is performed.

    feature_importances_ : ndarray of shape (n_features,)
        The feature importances (the higher, the more important the feature).

    oob_score_ : float
        Score of the training dataset obtained using an out-of-bag estimate.

    oob_decision_function_ : ndarray of shape (n_samples, n_classes)
        Decision function computed with out-of-bag estimate on the training
        set. If n_estimators is small it might be possible that a data point
        was never left out during the bootstrap. In this case,
        `oob_decision_function_` might contain NaN.

    See Also
    --------
    EasyEnsembleClassifier : Bag of balanced boosted learners.

    UnderBaggingClassifier : Bagging with intergrated random under-sampling.

    SelfPacedEnsembleClassifier : Ensemble with self-paced dynamic under-sampling.

    Notes
    -----
    See :ref:`sphx_glr_auto_examples_basic_plot_basic_example.py` for an example.

    References
    ----------
    .. [1] Chen, Chao, Andy Liaw, and Leo Breiman. "Using random forest to
       learn imbalanced data." University of California, Berkeley 110 (2004):
       1-12.

    Examples
    --------
    {example}
    """

    @_deprecate_positional_args
    def __init__(
        self,
        n_estimators=100,
        *,
        criterion="gini",
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        min_weight_fraction_leaf=0.0,
        max_features="auto",
        max_leaf_nodes=None,
        min_impurity_decrease=0.0,
        bootstrap=True,
        oob_score=False,
        replacement=False,
        n_jobs=None,
        random_state=None,
        verbose=0,
        warm_start=False,
        class_weight=None,
        ccp_alpha=0.0,
        max_samples=None,
    ):

        super().__init__(
            criterion=criterion,
            max_depth=max_depth,
            n_estimators=n_estimators,
            bootstrap=bootstrap,
            oob_score=oob_score,
            n_jobs=n_jobs,
            random_state=random_state,
            verbose=verbose,
            warm_start=warm_start,
            class_weight=class_weight,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            min_weight_fraction_leaf=min_weight_fraction_leaf,
            max_features=max_features,
            max_leaf_nodes=max_leaf_nodes,
            min_impurity_decrease=min_impurity_decrease,
            ccp_alpha=ccp_alpha,
            max_samples=max_samples,
        )

        self.__name__ = _method_name
        self._sampling_type = _sampling_type
        self._sampler_class = _sampler_class
        self._properties = _properties
        
        self.sampling_strategy = 'auto'
        self.replacement = replacement

    def _validate_estimator(self, default=DecisionTreeClassifier()):
        """Check the estimator and the n_estimator attribute, set the
        `base_estimator_` attribute."""
        if not isinstance(self.n_estimators, (numbers.Integral, np.integer)):
            raise ValueError(
                f"n_estimators must be an integer, " f"got {type(self.n_estimators)}."
            )

        if self.n_estimators <= 0:
            raise ValueError(
                f"n_estimators must be greater than zero, " f"got {self.n_estimators}."
            )

        if self.base_estimator is not None:
            self.base_estimator_ = clone(self.base_estimator)
        else:
            self.base_estimator_ = clone(default)

        self.base_sampler_ = RandomUnderSampler(
            sampling_strategy=self._sampling_strategy,
            replacement=self.replacement,
        )

    def _make_sampler_estimator(self, random_state=None):
        """Make and configure a copy of the `base_estimator_` attribute.
        Warning: This method should be used to properly instantiate new
        sub-estimators.
        """
        estimator = clone(self.base_estimator_)
        estimator.set_params(**{p: getattr(self, p) for p in self.estimator_params})
        sampler = clone(self.base_sampler_)

        if random_state is not None:
            _set_random_states(estimator, random_state)
            _set_random_states(sampler, random_state)

        return estimator, sampler

    @_deprecate_positional_args
    @FuncSubstitution(
        eval_datasets=_get_parameter_docstring('eval_datasets'),
        eval_metrics=_get_parameter_docstring('eval_metrics'),
        train_verbose=_get_parameter_docstring('train_verbose', **_properties),
    )
    def fit(self, X, y, 
            *, 
            sample_weight=None,
            eval_datasets:dict=None,
            eval_metrics:dict=None,
            train_verbose:bool=True,
            ):
        """Build a forest of trees from the training set (X, y).

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The training input samples. Internally, its dtype will be converted
            to ``dtype=np.float32``. If a sparse matrix is provided, it will be
            converted into a sparse ``csc_matrix``.

        y : array-like of shape (n_samples,) or (n_samples, n_outputs)
            The target values (class labels in classification, real numbers in
            regression).

        sample_weight : array-like of shape (n_samples,)
            Sample weights. If None, then samples are equally weighted. Splits
            that would create child nodes with net zero or negative weight are
            ignored while searching for a split in each node. In the case of
            classification, splits are also ignored if they would result in any
            single class carrying a negative weight in either child node.
        
        %(eval_datasets)s
        
        %(eval_metrics)s
        
        %(train_verbose)s

        Returns
        -------
        self : object
            The fitted instance.
        """

        # Validate or convert input data
        if issparse(y):
            raise ValueError("sparse multilabel-indicator for y is not supported.")
        
        check_x_y_args = {
            'accept_sparse': ['csc'],
            'multi_output': True,
            'dtype': DTYPE,
        }
        X, y = self._validate_data(X, y, **check_x_y_args)
        
        # Check evaluation data
        self.eval_datasets_ = check_eval_datasets(eval_datasets, X, y, **check_x_y_args)
        
        # Check evaluation metrics
        self.eval_metrics_ = check_eval_metrics(eval_metrics)

        # Check verbose
        self.train_verbose_ = check_train_verbose(
            train_verbose, self.n_estimators, **self._properties)
        self._init_training_log_format()

        if sample_weight is not None:
            sample_weight = _check_sample_weight(sample_weight, X)

        if issparse(X):
            # Pre-sort indices to avoid that each individual tree of the
            # ensemble sorts the indices.
            X.sort_indices()

        # Remap output
        _, self.n_features_ = X.shape

        y = np.atleast_1d(y)
        if y.ndim == 2 and y.shape[1] == 1:
            warn(
                "A column-vector y was passed when a 1d array was"
                " expected. Please change the shape of y to "
                "(n_samples,), for example using ravel().",
                DataConversionWarning,
                stacklevel=2,
            )

        if y.ndim == 1:
            # reshape is necessary to preserve the data contiguity against vs
            # [:, np.newaxis] that does not.
            y = np.reshape(y, (-1, 1))

        self.n_outputs_ = y.shape[1]

        y_encoded, expanded_class_weight = self._validate_y_class_weight(y)

        if getattr(y, "dtype", None) != DOUBLE or not y.flags.contiguous:
            y_encoded = np.ascontiguousarray(y_encoded, dtype=DOUBLE)

        if isinstance(self.sampling_strategy, dict):
            self._sampling_strategy = {
                np.where(self.classes_[0] == key)[0][0]: value
                for key, value in check_sampling_strategy(
                    self.sampling_strategy,
                    y,
                    "under-sampling",
                ).items()
            }
        else:
            self._sampling_strategy = self.sampling_strategy

        if expanded_class_weight is not None:
            if sample_weight is not None:
                sample_weight = sample_weight * expanded_class_weight
            else:
                sample_weight = expanded_class_weight

        # Get bootstrap sample size
        n_samples_bootstrap = _get_n_samples_bootstrap(
            n_samples=X.shape[0], max_samples=self.max_samples
        )

        # Check parameters
        self._validate_estimator()

        if not self.bootstrap and self.oob_score:
            raise ValueError("Out of bag estimation only available if bootstrap=True")

        random_state = check_random_state(self.random_state)

        if not self.warm_start or not hasattr(self, "estimators_"):
            # Free allocated memory, if any
            self.estimators_ = []
            self.estimators_n_training_samples_ = []
            self.samplers_ = []
            self.pipelines_ = []

        n_more_estimators = self.n_estimators - len(self.estimators_)

        if n_more_estimators < 0:
            raise ValueError(
                "n_estimators=%d must be larger or equal to "
                "len(estimators_)=%d when warm_start==True"
                % (self.n_estimators, len(self.estimators_))
            )

        elif n_more_estimators == 0:
            warn(
                "Warm-start fitting without increasing n_estimators does not "
                "fit new trees."
            )
        else:
            if self.warm_start and len(self.estimators_) > 0:
                # We draw from the random state to get the random state we
                # would have got if we hadn't used a warm_start.
                random_state.randint(MAX_INT, size=len(self.estimators_))

            trees = []
            samplers = []
            for _ in range(n_more_estimators):
                tree, sampler = self._make_sampler_estimator(random_state=random_state)
                trees.append(tree)
                samplers.append(sampler)

            # Parallel loop: we prefer the threading backend as the Cython code
            # for fitting the trees is internally releasing the Python GIL
            # making threading more efficient than multiprocessing in
            # that case. However, we respect any parallel_backend contexts set
            # at a higher level, since correctness does not rely on using
            # threads.
            samplers_trees = Parallel(
                n_jobs=self.n_jobs, verbose=self.verbose, prefer="threads"
            )(
                delayed(_local_parallel_build_trees)(
                    s,
                    t,
                    self,
                    X,
                    y_encoded,
                    sample_weight,
                    i,
                    len(trees),
                    verbose=self.verbose,
                    class_weight=self.class_weight,
                    n_samples_bootstrap=n_samples_bootstrap,
                )
                for i, (s, t) in enumerate(zip(samplers, trees))
            )
            samplers, trees, n_training_samples = zip(*samplers_trees)

            # Collect newly grown trees
            self.estimators_.extend(trees)
            self.samplers_.extend(samplers)
            self.estimators_n_training_samples_.extend(n_training_samples)

            # Create pipeline with the fitted samplers and trees
            self.pipelines_.extend(
                [
                    make_pipeline(deepcopy(s), deepcopy(t))
                    for s, t in zip(samplers, trees)
                ]
            )

        if self.oob_score:
            self._set_oob_score(X, y_encoded)

        # Decapsulate classes_ attributes
        if hasattr(self, "classes_") and self.n_outputs_ == 1:
            self.n_classes_ = self.n_classes_[0]
            self.classes_ = self.classes_[0]

        # Print training infomation to console.
        self._training_log_to_console()
        
        return self


    def _set_oob_score(self, X, y):
        """Compute out-of-bag score."""
        X = check_array(X, dtype=DTYPE, accept_sparse="csr")

        n_classes_ = self.n_classes_
        n_samples = y.shape[0]

        oob_decision_function = []
        oob_score = 0.0
        predictions = [
            np.zeros((n_samples, n_classes_[k])) for k in range(self.n_outputs_)
        ]

        for sampler, estimator in zip(self.samplers_, self.estimators_):
            X_resample = X[sampler.sample_indices_]
            y_resample = y[sampler.sample_indices_]

            n_sample_subset = y_resample.shape[0]
            n_samples_bootstrap = _get_n_samples_bootstrap(
                n_sample_subset, self.max_samples
            )

            unsampled_indices = _generate_unsampled_indices(
                estimator.random_state, n_sample_subset, n_samples_bootstrap
            )
            p_estimator = estimator.predict_proba(
                X_resample[unsampled_indices, :], check_input=False
            )

            if self.n_outputs_ == 1:
                p_estimator = [p_estimator]

            for k in range(self.n_outputs_):
                indices = sampler.sample_indices_[unsampled_indices]
                predictions[k][indices, :] += p_estimator[k]

        for k in range(self.n_outputs_):
            if (predictions[k].sum(axis=1) == 0).any():
                warn(
                    "Some inputs do not have OOB scores. "
                    "This probably means too few trees were used "
                    "to compute any reliable oob estimates."
                )

            with np.errstate(invalid="ignore", divide="ignore"):
                # with the resampling, we are likely to have rows not included
                # for the OOB score leading to division by zero
                decision = predictions[k] / predictions[k].sum(axis=1)[:, np.newaxis]
            mask_scores = np.isnan(np.sum(decision, axis=1))
            oob_decision_function.append(decision)
            oob_score += np.mean(
                y[~mask_scores, k] == np.argmax(predictions[k][~mask_scores], axis=1),
                axis=0,
            )

        if self.n_outputs_ == 1:
            self.oob_decision_function_ = oob_decision_function[0]
        else:
            self.oob_decision_function_ = oob_decision_function

        self.oob_score_ = oob_score / self.n_outputs_


    def _more_tags(self):
        return {"multioutput": False}


    @FuncGlossarySubstitution(_super.predict_log_proba, 'classes_')
    def predict_log_proba(self, X):
        return super().predict_log_proba(X)


    @FuncGlossarySubstitution(_super.predict_proba, 'classes_')
    def predict_proba(self, X):
        return super().predict_proba(X)


# %%

if __name__ == "__main__":
    from collections import Counter
    from copy import copy
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score
    
    # X, y = make_classification(n_classes=2, class_sep=2, # 2-class
    #     weights=[0.1, 0.9], n_informative=3, n_redundant=1, flip_y=0,
    #     n_features=20, n_clusters_per_class=1, n_samples=1000, random_state=10)
    X, y = make_classification(n_classes=3, class_sep=2, # 3-class
        weights=[0.1, 0.3, 0.6], n_informative=3, n_redundant=1, flip_y=0,
        n_features=20, n_clusters_per_class=1, n_samples=2000, random_state=10)

    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.5, random_state=42)

    origin_distr = dict(Counter(y_train)) # {2: 600, 1: 300, 0: 100}
    print('Original training dataset shape %s' % origin_distr)

    target_distr = {2: 200, 1: 100, 0: 100}

    init_kwargs_default = {
        # 'base_estimator': None,
        'n_estimators': 100,
        'criterion': "gini",
        'max_depth': None,
        'min_samples_split': 2,
        'min_samples_leaf': 1,
        'min_weight_fraction_leaf': 0.0,
        'max_features': "auto",
        'max_leaf_nodes': None,
        'min_impurity_decrease': 0.0,
        'bootstrap': True,
        'oob_score': False,
        'replacement': False,
        'n_jobs': None,
        'warm_start': False,
        'class_weight': None,
        'ccp_alpha': 0.0,
        'max_samples': None,
        'random_state': 42,
        # 'random_state': None,
        'verbose': 0,
    }
    fit_kwargs_default = {
        'X': X_train,
        'y': y_train,
        'sample_weight': None,
        'eval_datasets': {'valid': (X_valid, y_valid)},
        'eval_metrics': {
            'acc': (accuracy_score, {}),
            'balanced_acc': (balanced_accuracy_score, {}),
            'weighted_f1': (f1_score, {'average':'weighted'}),},
        'train_verbose': True,
    }

    ensembles = {}

    init_kwargs, fit_kwargs = copy(init_kwargs_default), copy(fit_kwargs_default)
    brf = BalancedRandomForestClassifier(**init_kwargs).fit(**fit_kwargs)
    ensembles['brf'] = brf


    # %%
    from visualizer import ImbalancedEnsembleVisualizer

    visualizer = ImbalancedEnsembleVisualizer(
        eval_datasets = None,
        eval_metrics = None,
    ).fit(
        ensembles = ensembles,
        granularity = 5,
    )
    fig, axes = visualizer.performance_lineplot(
        on_ensembles=None,
        on_datasets=None,
        split_by=[],
        n_samples_as_x_axis=False,
        sub_figsize=(4, 3.3),
        sup_title=True,
        alpha=0.8,
    )
    fig, axes = visualizer.confusion_matrix_heatmap(
        on_ensembles=None,
        on_datasets=None,
        sub_figsize=(4, 3.3),
    )
    
    # %%