# Return the softmax of an input 1D array.
# You can use numpy or pytorch.

import numpy as np

# import torch


def softmax(x):
    # e^(x_i - c) / sum(e^(x_i - c)) =
    # x_i - log sum(e^x_i)
    # e^x ~= 1 + x + o(x)
    # sum(e^x_i) = n + sum(x_i) + 1/2 sum(x_i^2)
    max_x = np.max(x)
    x -= max_x
    softmax_x = np.exp(x)
    softmax_x = softmax_x / np.sum(np.exp(x))
    return softmax_x


# x = torch.tensor(x)
print(softmax([1, 2, 3, 4000]))
