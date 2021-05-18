import torch
import torch.nn as nn


class RobustScannerFusionLayer(nn.Module):

    def __init__(self, dim_model, dim=-1):
        super().__init__()

        self.dim_model = dim_model
        self.dim = dim

        self.linear_layer = nn.Linear(dim_model * 2, dim_model * 2)
        self.glu_layer = nn.GLU(dim=dim)

    def forward(self, x0, x1):
        assert x0.size() == x1.size()
        fusion_input = torch.cat([x0, x1], self.dim)
        output = self.linear_layer(fusion_input)
        output = self.glu_layer(output)

        return output
