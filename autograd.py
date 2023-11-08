import torch

'''
def grad(_y, _x):
    _y.backward()
    return _x.grad
'''

a = torch.tensor(3, requires_grad=True,dtype=torch.float32)
b = torch.tensor(4, requires_grad=True,dtype=torch.float32)
x = torch.tensor(5, requires_grad=True,dtype=torch.float32)

# make graph y = ax + b
y = a * x + b
print(y)

y.backward()

print(a.grad)
print(b.grad)
print(x.grad)
# キモいけど↑使ったほうが良さそう

'''
print(grad(y,a))
print(grad(y,b))
print(grad(y,b))
'''