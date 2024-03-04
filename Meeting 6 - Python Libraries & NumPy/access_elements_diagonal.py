import numpy as np

# 2D array
array_2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

print("\nPrint 2D array")
print(array_2d)

print("\nAccess elements in diagonal form (column 2)")
print(array_2d.diagonal(2))

print("\nAccess elements in diagonal form (column 4)")
print(array_2d.diagonal(4))
