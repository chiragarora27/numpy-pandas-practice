import numpy as np

a = np.full([3, 2], 2)
b = np.full([2, 3], 1)

print(np.matmul(b, a))


# determinant
c = np.identity(3)
print(np.linalg.det(c))

# eigenvalue
print(np.linalg.eigvals(c))

# trace
print(np.linalg.trace(c))

# inverse
print(np.linalg.inv(c))
