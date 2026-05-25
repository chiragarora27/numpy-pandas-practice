import numpy as np

# reshape
before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])


after = np.reshape(before, [4, 2])


# vertically stacking vectors

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack([v1, v2]))

# horizontal stack similar - hstack
