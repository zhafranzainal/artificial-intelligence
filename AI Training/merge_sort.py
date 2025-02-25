def merge_sort(array):
    if len(array) <= 1:
        return array

    # Divide the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    # Merge two sorted arrays
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


# Example usage:
unsorted_array = [5, 2, 4, 6, 1, 3]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)  # Output: [1, 2, 3, 4, 5, 6]
