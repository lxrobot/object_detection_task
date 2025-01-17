from torch import nn
from torch import Tensor

class Residual(nn.Module):
    def __init__(self, sublayer: nn.Module, dimension: int, dropout: float = 0.1):
        super().__init__()
        self.sublayer = sublayer
        self.norm = nn.LayerNorm(dimension)
        self.dropout = nn.Dropout(dropout)

    def forward(self, *tensors: Tensor) -> Tensor:
        # Assume that the "value" tensor is given last, so we can compute the
        # residual.  This matches the signature of 'MultiHeadAttention'.
        if len(tensors) == 1:
            print(f"*tensors: {tensors[-1].shape}")
        return self.norm(tensors[-1] + self.dropout(self.sublayer(*tensors)))
