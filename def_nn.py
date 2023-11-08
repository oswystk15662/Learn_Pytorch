import torch
from torch import nn

net = nn.Sequential(
    nn.Conv2d(1,6,3),
    nn.MaxPool2d((2,2)),
    nn.ReLU(),
    nn.Conv2d(6,16,3),
    nn.MaxPool2d(2), # (2,2)と同じらしい、正方形ならこれが使える
    nn.ReLU()
)

print(net)