import numpy as np

# array with all 0s

new = np.zeros([2, 2])  # shape
# print(new)

new = np.ones([2, 2])
# print(new)

new = np.full([2, 2], 9)
# print(new)

new2 = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

new = np.full_like(new2, 5)
# print(new)

new = np.full(new2.shape, 6)
# print(new)

# array of random decimals
new = np.random.rand(2, 6)
print(new)

new = np.random.random_sample(new2.shape)
# print(new)

new = np.random.randint(-2, 8, size=(3, 3))
# print(new)

# identity matrix
new = np.identity(3)

# repeating array

new3 = np.array([[1, 2, 3]])

# r1 = np.repear(name of array we need to repeat, number of times, axis)
r1 = np.repeat(new3, 3, axis=0)

a2 = np.zeros([3, 3])
a3 = np.ones([5, 5])

a3[1:4, 1:4] = a2
a3[2, 2] = 9

# print(a3)

# to copy, use copy() function otherwise, only variable name will change

# the wrong way
a = [1, 2, 3]
b = a
print(b)
b[0] = 10
print(b)
print(a)

# the right way
x = [1, 2, 3]
y = x.copy()
print(y)
y[0] = 10
print(y)
print(x)
