import numpy as np

c = np.array([3, 6, 9, 12])
d = np.array([2, 4, 6, 8])

print("\nArray #1")
print(c)

print("\nArray #2")
print(d)

print("\nArray #1 + Array #2")
print(np.add(c, d))

print("\nArray #1 - Array #2")
print(np.subtract(c, d))

print("\nArray #1 * Array #2")
print(np.multiply(c, d))

print("\nArray #1 / Array #2")
print(np.divide(c, d))

print("\nSummation of elements in Array #1 & Array #2, respectively")
print(c.sum(), d.sum())

print("\nMinimum value in Array #1 & Array #2, respectively")
print(c.min(), d.min())

print("\nMaximum value in Array #1 & Array #2, respectively")
print(c.max(), d.max())
