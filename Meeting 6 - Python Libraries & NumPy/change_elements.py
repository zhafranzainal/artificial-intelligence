import numpy as np

print("\nInitialize empty array")
empty = np.zeros((4, 4), dtype="int")
print(empty)

print("\nFill numbers for row 0, column 1 till 3")
empty[0, 1:4] = [1, 55, 3]
print(empty)

print("\nFill number for last row, column 0")
empty[-1, 0] = 7
print(empty)

print("\nFill numbers for column 1 on row 1 till 2")
empty[1:3, 1] = [9, 5]
print(empty)

print("\nFill numbers for right bottom corner")
empty[2:4, 2:4] = [
    [0, 70],
    [14, 22]
]
print(empty)
