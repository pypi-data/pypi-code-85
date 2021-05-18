# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02 - layers.ipynb (unless otherwise specified).

__all__ = ['PoolingType', '_splitter', 'create_fastai_encoder', 'create_timm_encoder', 'create_encoder',
           'create_mlp_module', 'create_cls_module', 'create_model', 'CheckpointResNet', 'CheckpointEfficientNet',
           'CheckpointVisionTransformer', 'CheckpointSequential']

# Cell
from fastai.vision.all import *
import timm

# Cell
# https://github.com/rwightman/pytorch-image-models/blob/3a7aa95f7e5fc90a6a2683c756e854e26201d82e/timm/models/layers/adaptive_avgmax_pool.py#L79
mk_class('PoolingType', **{o:o.lower() for o in ['Fast', 'Avg', 'AvgMax', 'CatAvgMax', 'Max']},
         doc="All possible pooling types as attributes to get tab-completion and typo-proofing")

# Cell
#nbdev_comment _all_ = ['PoolingType', '_splitter']

# Cell
def create_fastai_encoder(arch:str, pretrained=True, n_in=3, pool_type=PoolingType.CatAvgMax):
    "Create timm encoder from a given arch backbone"
    encoder = create_body(arch, n_in, pretrained, cut=None)
    pool = AdaptiveConcatPool2d() if pool_type == "catavgmax" else nn.AdaptiveAvgPool2d(1)
    return nn.Sequential(*encoder, pool, Flatten())

def create_timm_encoder(arch:str, pretrained=True, n_in=3, pool_type=PoolingType.CatAvgMax):
    "Creates a body from any model in the `timm` library. If pool_type is None then it uses timm default"
    if ('vit' in arch) or (pool_type is None):
        model = timm.create_model(arch, pretrained=pretrained, in_chans=n_in, num_classes=0)
    else:
        model = timm.create_model(arch, pretrained=pretrained, in_chans=n_in, num_classes=0, global_pool=pool_type)
    return model

def create_encoder(arch:str, pretrained=True, n_in=3, pool_type=PoolingType.CatAvgMax):
    "A utility for creating encoder without specifying the package"
    if arch in globals(): return create_fastai_encoder(globals()[arch], pretrained, n_in, pool_type)
    else:                 return create_timm_encoder(arch, pretrained, n_in, pool_type)

# Cell
def create_mlp_module(dim,hidden_size,projection_size,bn=False,nlayers=2):
    "MLP module as described in papers, used as projection layer"
    l = []
    for i in range(nlayers-1):
        l += [nn.Linear(dim, hidden_size) if i == 0 else nn.Linear(hidden_size, hidden_size)]
        if bn: l += [nn.BatchNorm1d(hidden_size)]
        l += [nn.ReLU(inplace=True)]
    ls = l + [nn.Linear(hidden_size, projection_size)]
    return nn.Sequential(*ls)

# Cell
def create_cls_module(nf, n_out, lin_ftrs=None, ps=0.5, use_bn=True, first_bn=True, bn_final=False, lin_first=False, y_range=None):
    "Creates classification layer which takes nf flatten features and outputs n_out logits"
    lin_ftrs = [nf, 512, n_out] if lin_ftrs is None else [nf] + lin_ftrs + [n_out]
    bns = [first_bn] + [use_bn]*len(lin_ftrs[1:])
    ps = L(ps)
    if len(ps) == 1: ps = [ps[0]/2] * (len(lin_ftrs)-2) + ps
    actns = [nn.ReLU(inplace=True)] * (len(lin_ftrs)-2) + [None]
    layers = []
    if lin_first: layers.append(nn.Dropout(ps.pop(0)))
    for ni,no,bn,p,actn in zip(lin_ftrs[:-1], lin_ftrs[1:], bns, ps, actns):
        layers += LinBnDrop(ni, no, bn=bn, p=p, act=actn, lin_first=lin_first)
    if lin_first: layers.append(nn.Linear(lin_ftrs[-2], n_out))
    if bn_final: layers.append(nn.BatchNorm1d(lin_ftrs[-1], momentum=0.01))
    if y_range is not None: layers.append(SigmoidRange(*y_range))
    return nn.Sequential(*layers)

# Cell
@delegates(create_cls_module)
def create_model(arch, n_out, pretrained=True, n_in=3, pool_type=PoolingType.CatAvgMax, **kwargs):
    encoder = create_encoder(arch, pretrained=pretrained, n_in=n_in, pool_type=pool_type)
    sz = int(arch.split("_")[-1]) if 'vit'in arch else 224
    with torch.no_grad(): nf = encoder(torch.randn(2,3,sz,sz)).size(-1)
    head = create_cls_module(nf, n_out, **kwargs)
    apply_init(head)
    model = nn.Sequential(encoder, head)
    return model

# Cell
def _splitter(m): return L(m[0], m[1]).map(params)

# Cell
from torch.utils.checkpoint import checkpoint_sequential

class CheckpointResNet(Module):
    def __init__(self, resnet_model, checkpoint_nchunks=2):
        "A gradient checkpoint wrapper for timm ResNet"
        self.checkpoint_nchunks = checkpoint_nchunks
        self.resnet_model = resnet_model
        self.forward_layers = nn.Sequential(*[
            self.resnet_model.layer1,
            self.resnet_model.layer2,
            self.resnet_model.layer3,
            self.resnet_model.layer4
        ])

    def forward(self, x):
        x = self.resnet_model.conv1(x)
        x = self.resnet_model.bn1(x)
        x = self.resnet_model.act1(x)
        x = self.resnet_model.maxpool(x)

        x = checkpoint_sequential(self.forward_layers, self.checkpoint_nchunks, x)
        x = self.resnet_model.global_pool(x)

        if self.resnet_model.drop_rate:
            x = F.dropout(x, p=float(self.resnet_model.drop_rate), training=self.resnet_model.training)
        x = self.resnet_model.fc(x)
        return x

class CheckpointEfficientNet(Module):
    def __init__(self, effnet_model, checkpoint_nchunks=2):
        "A gradient checkpoint wrapper for timm EfficientNet"
        self.checkpoint_nchunks = checkpoint_nchunks
        self.effnet_model = effnet_model

    def forward_features(self, x):
        x = self.effnet_model.conv_stem(x)
        x = self.effnet_model.bn1(x)
        x = self.effnet_model.act1(x)
        x = checkpoint_sequential(self.effnet_model.blocks, self.checkpoint_nchunks, x)
        x = self.effnet_model.conv_head(x)
        x = self.effnet_model.bn2(x)
        x = self.effnet_model.act2(x)
        return x

    def forward(self, x):
        x = self.forward_features(x)
        x = self.effnet_model.global_pool(x)
        if self.effnet_model.drop_rate > 0.:
            x = F.dropout(x, p=self.effnet_model.drop_rate, training=self.effnet_model.training)
        return self.effnet_model.classifier(x)

class CheckpointVisionTransformer(Module):
    def __init__(self, vit_model, checkpoint_nchunks=2):
        "A gradient checkpoint wrapper for timm VisionTransformer"
        self.checkpoint_nchunks = checkpoint_nchunks
        self.vit_model = vit_model

    def forward_features(self, x):
        B = x.shape[0]
        x = self.vit_model.patch_embed(x)

        cls_tokens = self.vit_model.cls_token.expand(B, -1, -1)  # stole cls_tokens impl from Phil Wang, thanks
        x = torch.cat((cls_tokens, x), dim=1)
        x = x + self.vit_model.pos_embed
        x = self.vit_model.pos_drop(x)
        x = checkpoint_sequential(self.vit_model.blocks, self.checkpoint_nchunks, x)
        x = self.vit_model.norm(x)[:, 0]
        x = self.vit_model.pre_logits(x)
        return x

    def forward(self, x):
        x = self.forward_features(x)
        x = self.vit_model.head(x)
        return x

class CheckpointSequential(Module):
    def __init__(self, fastai_model, checkpoint_nchunks=2):
        "A gradient checkpoint wrapper for nn.Sequential"
        self.checkpoint_nchunks = checkpoint_nchunks
        self.fastai_model = fastai_model

    def forward(self, x):
        x = checkpoint_sequential(self.fastai_model, self.checkpoint_nchunks, x)
        return x