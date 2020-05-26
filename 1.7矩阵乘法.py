import torch
import numpy as np

data = [[1,2],[3,4]]
tensor = torch.FloatTensor(data)
data = np.array(data)
print(
    '\nnumpy:',np.matmul(data,data),
    '\nnumpy:',data.dot(data),
    '\ntorch:',torch.mm(tensor,tensor),

)