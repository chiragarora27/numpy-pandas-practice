import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])

print(np.min(stats))

print(np.min(stats, axis=0), np.min(stats, axis=1))

# same for max and sum
# std deviation
