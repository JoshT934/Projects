import numpy as np

# activation function and its derivative, for housekeeping,
# can take any other common activation function, such as ReLu
def tanh(x):
    return np.tanh(x)


def tanh_prime(x):
    return 1-np.tanh(x)**2