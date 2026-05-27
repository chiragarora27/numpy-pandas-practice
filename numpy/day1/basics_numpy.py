import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[2.2, 3.3, 4.4], [1.1, 5.5, 6.6]])
print(b)

print(a.ndim)
print(b.ndim)

# shape is basically rows * columns for a 2d array
print(a.shape)
print(b.shape)

new = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

print(new[1, 5])  # print(new[1][5]) also works

print(new[0, :])  # print(new[0]) also works

# [startindex : endindex : stepsize]


print(new[0, 1:6:2])

three_d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

three_d[0, 1, 1] = 14

three_d[:, 0, :] = [[11, 11], [22, 22]]

print(three_d)
