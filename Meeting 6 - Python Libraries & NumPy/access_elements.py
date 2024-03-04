import numpy as np

# 2D array
array_2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

print("\nPrint 2D array")
print(array_2d)

print("\nAccess elements in 2D array (row no 1)")
print(array_2d[1, :])

print("\nAccess elements in 2D array (column no 1)")
print(array_2d[:, 1])
