import numpy as np

# 2D array
array_2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

print("\nPrint 2D array")
print(array_2d)

print("\nSlice array for column 1 until 2")
print(array_2d[:, 1:3])

print("\nSlice array for row 1, column 1 until 3")
print(array_2d[1, 1:4])

print("\nSlice array for row 0 until 1, column 1 until 3")
print(array_2d[:2, 1:4])
