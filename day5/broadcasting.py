import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 2, 3])

# print(a+b) - shows error as a and b are not compatible

c = np.array([2])

# print(a+c) - shows no error since c is 1x1


x = np.array([[1, 1, 1, 1], [2, 2, 2, 2]])
y = np.array([1, 0, 1, 0])

# print(x+y) - x is 2d while y is 1d still no error as y is stretched to 2d and the result is that of the highest dimension
# among the inputs
