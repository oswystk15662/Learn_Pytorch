'''
tensor +-*/ tensor ok
tensor +-*/ nparray dame

tensor同士の四則演算で次元が違うと自動補完されることがある。。。
'''

import torch

a = torch.tensor([[1,2,3], [4,5,6]], dtype= torch.float32)
'''print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)'''

b = torch.tensor([[2,4,6],[8,10,12]], dtype=torch.float32)
'''print(a+b)
print(a-b)
print(a*b)
print(a/b)'''

print(torch.max(a))
print(torch.min(a))
print(torch.mean(a))
print(torch.sum(a))
print(torch.sum(a).item())