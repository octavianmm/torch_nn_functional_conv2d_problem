import torch
import sys

input = torch.load("input_tensor.pt")
weight = torch.load("weight.pt")
bias=None
stride=(1,1)
padding=(0,0)
dilation=(1,1)
groups=1

output = torch.nn.functional.conv2d(input, weight, bias, stride, padding, dilation, groups)
torch.save(output, "output_tensor.pt")
torch.set_printoptions(profile="full")

with open('output_tensor.txt',  'w') as f:
    sys.stdout = f
    print(output)
