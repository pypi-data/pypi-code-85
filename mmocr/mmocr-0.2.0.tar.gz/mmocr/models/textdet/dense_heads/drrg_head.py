import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from mmcv.cnn import normal_init

from mmdet.models.builder import HEADS, build_loss
from mmocr.models.textdet.modules import GCN, LocalGraphs, ProposalLocalGraphs
from mmocr.models.textdet.postprocess import decode
from mmocr.utils import check_argument
from .head_mixin import HeadMixin


@HEADS.register_module()
class DRRGHead(HeadMixin, nn.Module):
    """The class for DRRG head: Deep Relational Reasoning Graph Network for
    Arbitrary Shape Text Detection.

    [https://arxiv.org/abs/2003.07493]

    Args:
        k_at_hops (tuple(int)): The number of i-hop neighbors, i = 1, 2.
        num_adjacent_linkages (int): The number of linkages when constructing
            adjacent matrix.
        node_geo_feat_len (int): The length of embedded geometric feature
            vector of a component.
        pooling_scale (float): The spatial scale of rotated RoI-Align.
        pooling_output_size (tuple(int)): The output size of RRoI-Aligning.
        nms_thr (float): The locality-aware NMS threshold of text components.
        min_width (float): The minimum width of text components.
        max_width (float): The maximum width of text components.
        comp_shrink_ratio (float): The shrink ratio of text components.
        comp_ratio (float): The reciprocal of aspect ratio of text components.
        comp_score_thr (float): The score threshold of text components.
        text_region_thr (float): The threshold for text region probability map.
        center_region_thr (float): The threshold for text center region
            probability map.
        center_region_area_thr (int): The threshold for filtering small-sized
            text center region.
        local_graph_thr (float): The threshold to filter identical local
            graphs.
        link_thr(float): The threshold for connected components search.
    """

    def __init__(self,
                 in_channels,
                 k_at_hops=(8, 4),
                 num_adjacent_linkages=3,
                 node_geo_feat_len=120,
                 pooling_scale=1.0,
                 pooling_output_size=(4, 3),
                 nms_thr=0.3,
                 min_width=8.0,
                 max_width=24.0,
                 comp_shrink_ratio=1.03,
                 comp_ratio=0.4,
                 comp_score_thr=0.3,
                 text_region_thr=0.2,
                 center_region_thr=0.2,
                 center_region_area_thr=50,
                 local_graph_thr=0.7,
                 link_thr=0.85,
                 loss=dict(type='DRRGLoss'),
                 train_cfg=None,
                 test_cfg=None):
        super().__init__()

        assert isinstance(in_channels, int)
        assert isinstance(k_at_hops, tuple)
        assert isinstance(num_adjacent_linkages, int)
        assert isinstance(node_geo_feat_len, int)
        assert isinstance(pooling_scale, float)
        assert isinstance(pooling_output_size, tuple)
        assert isinstance(comp_shrink_ratio, float)
        assert isinstance(nms_thr, float)
        assert isinstance(min_width, float)
        assert isinstance(max_width, float)
        assert isinstance(comp_ratio, float)
        assert isinstance(comp_score_thr, float)
        assert isinstance(text_region_thr, float)
        assert isinstance(center_region_thr, float)
        assert isinstance(center_region_area_thr, int)
        assert isinstance(local_graph_thr, float)
        assert isinstance(link_thr, float)

        self.in_channels = in_channels
        self.out_channels = 6
        self.downsample_ratio = 1.0
        self.k_at_hops = k_at_hops
        self.num_adjacent_linkages = num_adjacent_linkages
        self.node_geo_feat_len = node_geo_feat_len
        self.pooling_scale = pooling_scale
        self.pooling_output_size = pooling_output_size
        self.comp_shrink_ratio = comp_shrink_ratio
        self.nms_thr = nms_thr
        self.min_width = min_width
        self.max_width = max_width
        self.comp_ratio = comp_ratio
        self.comp_score_thr = comp_score_thr
        self.text_region_thr = text_region_thr
        self.center_region_thr = center_region_thr
        self.center_region_area_thr = center_region_area_thr
        self.local_graph_thr = local_graph_thr
        self.link_thr = link_thr
        self.loss_module = build_loss(loss)
        self.train_cfg = train_cfg
        self.test_cfg = test_cfg

        self.out_conv = nn.Conv2d(
            in_channels=self.in_channels,
            out_channels=self.out_channels,
            kernel_size=1,
            stride=1,
            padding=0)
        self.init_weights()

        self.graph_train = LocalGraphs(self.k_at_hops,
                                       self.num_adjacent_linkages,
                                       self.node_geo_feat_len,
                                       self.pooling_scale,
                                       self.pooling_output_size,
                                       self.local_graph_thr)

        self.graph_test = ProposalLocalGraphs(
            self.k_at_hops, self.num_adjacent_linkages, self.node_geo_feat_len,
            self.pooling_scale, self.pooling_output_size, self.nms_thr,
            self.min_width, self.max_width, self.comp_shrink_ratio,
            self.comp_ratio, self.comp_score_thr, self.text_region_thr,
            self.center_region_thr, self.center_region_area_thr)

        pool_w, pool_h = self.pooling_output_size
        node_feat_len = (pool_w * pool_h) * (
            self.in_channels + self.out_channels) + self.node_geo_feat_len
        self.gcn = GCN(node_feat_len)

    def init_weights(self):
        normal_init(self.out_conv, mean=0, std=0.01)

    def forward(self, inputs, gt_comp_attribs):

        pred_maps = self.out_conv(inputs)
        feat_maps = torch.cat([inputs, pred_maps], dim=1)
        node_feats, adjacent_matrices, knn_inds, gt_labels = self.graph_train(
            feat_maps, np.stack(gt_comp_attribs))

        gcn_pred = self.gcn(node_feats, adjacent_matrices, knn_inds)

        return pred_maps, (gcn_pred, gt_labels)

    def single_test(self, feat_maps):

        pred_maps = self.out_conv(feat_maps)
        feat_maps = torch.cat([feat_maps, pred_maps], dim=1)

        none_flag, graph_data = self.graph_test(pred_maps, feat_maps)

        (local_graphs_node_feat, adjacent_matrices, pivots_knn_inds,
         pivot_local_graphs, text_comps) = graph_data

        if none_flag:
            return None, None, None

        gcn_pred = self.gcn(local_graphs_node_feat, adjacent_matrices,
                            pivots_knn_inds)
        pred_labels = F.softmax(gcn_pred, dim=1)

        edges = []
        scores = []
        pivot_local_graphs = pivot_local_graphs.long().squeeze().cpu().numpy()

        for pivot_ind, pivot_local_graph in enumerate(pivot_local_graphs):
            pivot = pivot_local_graph[0]
            for k_ind, neighbor_ind in enumerate(pivots_knn_inds[pivot_ind]):
                neighbor = pivot_local_graph[neighbor_ind.item()]
                edges.append([pivot, neighbor])
                scores.append(
                    pred_labels[pivot_ind * pivots_knn_inds.shape[1] + k_ind,
                                1].item())

        edges = np.asarray(edges)
        scores = np.asarray(scores)

        return edges, scores, text_comps

    def get_boundary(self, edges, scores, text_comps, img_metas, rescale):
        """Compute text boundaries via post processing.

        Args:
            edges (ndarray): The edge array of shape N * 2, each row is a pair
                of text component indices that makes up an edge in graph.
            scores (ndarray): The edge score array.
            text_comps (ndarray): The text components.
            img_metas (list[dict]): The image meta infos.
            rescale (bool): Rescale boundaries to the original image
                resolution.

        Returns:
            results (dict): The result dict.
        """

        assert check_argument.is_type_list(img_metas, dict)
        assert isinstance(rescale, bool)

        boundaries = []
        if edges is not None:
            boundaries = decode(
                decoding_type='drrg',
                edges=edges,
                scores=scores,
                text_comps=text_comps,
                link_thr=self.link_thr)
        if rescale:
            boundaries = self.resize_boundary(
                boundaries,
                1.0 / self.downsample_ratio / img_metas[0]['scale_factor'])

        results = dict(boundary_result=boundaries)

        return results
