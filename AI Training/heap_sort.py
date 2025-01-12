def heapify(array, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child position
    right = 2 * i + 2  # Right child position

    # Check if left child exists and is greater than root
    if left < n and array[left] > array[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and array[right] > array[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # Swap

        # Heapify the root.
        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Swap
        heapify(array, i, 0)


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
heap_sort(arr)
print("Sorted array:", arr)
