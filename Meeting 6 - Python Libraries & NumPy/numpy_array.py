import numpy as np

# 1D array
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
c = np.array(["test", 11, 11.5])

# 2D array
array_2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

# 3D array
array_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
    [[13, 14, 15], [16, 17, 18]]
])

print("\n1D array")
print(a)
print(b)
print(c)

print("\n2D array")
print(array_2d)

print("\n3D array\n")
print(array_3d)

print("\nPrint 2D array")
print(array_2d)

print("\nSee shape of 2D array (Row vs Column)")
print(array_2d.shape)

print("\nAccess specific element in 2D array (num 4)")
print(array_2d[0, 3])

print("\nAccess specific element in 2D array (num 7)")
print(array_2d[1, 1])

print("\nAccess elements in 2D array (row no 1)")
print(array_2d[1, :])

print("\nAccess elements in 2D array (column no 1)")
print(array_2d[:, 1])