import numpy as np

# exercise 1
# a = np.array([1, 2, 3, 4, 5])

# print(a.shape)
# print(a.ndim)
# print(a.dtype)
# print(a.size)

# exercise 2
# a = np.array([[1, 2, 3], [4, 5, 6]])
# print(a[1, :])
# print(a[:, 2])
# print(a[1, 1])

# exercise 3
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# a[a % 2 == 0] = 0
# print(a)

# exercise 4
# a = np.zeros([3, 3])
# a[[0, 2], ([0, 2], [2, 0])] = 1
# a[1, 1] = 5
# print(a)

# exercise 5
# arr = np.array([1, 2, 3, 4])
# arr = arr + 10
# arr = arr * 3
# print(arr)

# exercise 6 - output prediction
# a = np.array([[1], [2], [3]])
# b = np.array([10, 20, 30])

# c = a + b
# print(c)

# exercise 7
# a = np.random.randint(1, 100, size=[4, 4])

# b = np.mean(a, axis=1)
# print(a)
# print(b)

# b = np.reshape(b, [4, 1])
# c = a - b
# print(c)

# exercise 8
# arr = np.array([4, 7, 1, 9, 12, 3, 15])

# b = arr[arr > 5]
# c = arr[~(arr % 2 == 0)]
# d = arr[(arr > 5) & (arr < 12)]

# print(b)
# print(c)
# print(d)

# exercise 9
# a = np.random.randint(1, 100, size=[20, ])
# a[a < 50] = -1

# print(a)

# exercise 10
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(np.sum(a, axis=1))
# print(np.sum(a, axis=0))
# print(np.mean(a, axis=1))
# print(np.mean(a, axis=0))


# exercise 11
# a = np.random.rand(5, 4)
# print(np.max(a, axis=1))
# print(np.min(a, axis=0))
# exercise 12
# a = np.array([n for n in range(1, 25)])

# b = np.reshape(a, shape=[2, 12])
# print(b)

# c = np.reshape(a, shape=[3, 8])
# print(c)

# d = np.reshape(a, shape=[4, 6])
# print(d)

# e = np.reshape(a, shape=[2, 3, 4])
# print(e)

# exercise 13
# a = np.array([[1, 2, 3], [4, 5, 6]])

# b = np.reshape(a, -1)
# print(b)

# c = a.flatten()
# print(c)

# exercise 14
# a = np.ones([4, 4])
# a[[0, 1, 2, 3, 2, 3, 0, 1], [0, 1, 2, 3, 0, 1, 2, 3]] = 0
# print(a)

# excercise 15
# assuming each row is one student and each column is one subject

# a = np.array([[85, 90, 78],
#               [92, 88, 95],
#               [70, 76, 80]
#               ])

# print(np.average(a, axis=1))
# print(np.average(a, axis=0))

# b = np.sum(a, axis=1)
# print(np.where(b == np.max(b)))


a = np.zeros(shape=[5, 3])

b = np.ones(shape=[3,])

c = a + b
print(c.shape)
