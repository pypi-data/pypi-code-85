import unittest

import numpy as np
import tensorflow as tf

from kgcnn.layers.pooling import PoolingLocalEdgesLSTM
from kgcnn.layers.casting import ChangeTensorType, ChangeIndexing
from kgcnn.layers.gather import GatherNodes
from kgcnn.layers.keras import Concatenate

class TestPoolingLocalEdgesLSTM(unittest.TestCase):

    n1 = [[[1.0], [6.0], [1.0], [6.0], [1.0], [1.0], [6.0], [6.0]],
          [[6.0], [1.0], [1.0], [1.0], [7.0], [1.0], [6.0], [8.0], [6.0], [1.0], [6.0], [7.0], [1.0], [1.0], [1.0]]]
    ei1 = [[[0, 1], [1, 0], [1, 6], [2, 3], [3, 2], [3, 5], [3, 7], [4, 7], [5, 3], [6, 1], [6, 7], [7, 3], [7, 4],
            [7, 6]],
           [[0, 6], [0, 8], [0, 9], [1, 11], [2, 4], [3, 4], [4, 2], [4, 3], [4, 6], [5, 10], [6, 0], [6, 4], [6, 14],
            [7, 8], [8, 0], [8, 7], [8, 11], [9, 0], [10, 5], [10, 11], [10, 12], [10, 13], [11, 1], [11, 8], [11, 10],
            [12, 10], [13, 10], [14, 6]]]
    e1 = [[[0.408248290463863], [0.408248290463863], [0.3333333333333334], [0.35355339059327373], [0.35355339059327373],
           [0.35355339059327373], [0.25], [0.35355339059327373], [0.35355339059327373], [0.3333333333333334],
           [0.2886751345948129], [0.25], [0.35355339059327373], [0.2886751345948129]],
          [[0.25], [0.25], [0.35355339059327373], [0.35355339059327373], [0.35355339059327373], [0.35355339059327373],
           [0.35355339059327373], [0.35355339059327373], [0.25], [0.3162277660168379], [0.25], [0.25],
           [0.35355339059327373], [0.35355339059327373], [0.25], [0.35355339059327373], [0.25], [0.35355339059327373],
           [0.3162277660168379], [0.22360679774997896], [0.3162277660168379], [0.3162277660168379],
           [0.35355339059327373], [0.25], [0.22360679774997896], [0.3162277660168379], [0.3162277660168379],
           [0.35355339059327373]]]

    def test_pooling_LSTM(self):
        node = tf.ragged.constant(self.n1, ragged_rank=1, inner_shape=(1,))
        edgeind = tf.ragged.constant(self.ei1, ragged_rank=1, inner_shape=(2,))
        edgefeat = tf.ragged.constant(self.e1, ragged_rank=1, inner_shape=(1,))


        node_indexing = 'sample'
        partition_type = 'row_length'
        tens_type = "values_partition"
        n = ChangeTensorType(input_tensor_type="ragged", output_tensor_type=tens_type)(node)
        ed = ChangeTensorType(input_tensor_type="ragged", output_tensor_type=tens_type)(edgefeat)
        edi = ChangeTensorType(input_tensor_type="ragged", output_tensor_type=tens_type)(edgeind)
        edi = ChangeIndexing(input_tensor_type=tens_type, to_indexing=node_indexing)([n, edi])



        ns = GatherNodes(input_tensor_type=tens_type, node_indexing=node_indexing,
                         partition_type=partition_type)([n, edi])
        messages = Concatenate(axis=-1, input_tensor_type=tens_type)([ed,ns])
        out = PoolingLocalEdgesLSTM(units=3, input_tensor_type=tens_type,
                                    node_indexing=node_indexing)([n, messages, edi])
        self.assertTrue(np.all(np.array(out[0].shape) == np.array([23,3])))


if __name__ == '__main__':
    unittest.main()


