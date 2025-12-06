import numpy as np


# Fast arrays

# Fast math

# Tools for linear algebra, statistics, random numbers

# creating arrays

arr = np.array([1, 2, "sujan", True])
print(arr)
print(arr[1])
print(arr[3])
print(type(arr))  # numpy.ndarray

# multi dimensional array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[0][1])
print(b.shape)  # 2*3 matrix (size of matrix)
print(b.dtype)

print(np.zeros((3, 4)))  # zero matrix
print(np.ones((3, 4)))  # one matrix of 3*4
