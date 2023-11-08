import torch
import numpy as np

a = np.array([[1,2,3], [4,5,6]])
print(a)

b = torch.from_numpy(a)
print(b)

print(a[1,2])
print(a[0,:])

c = b.view(3,2)
print(c)