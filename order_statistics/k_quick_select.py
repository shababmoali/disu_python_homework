import random


def quick_select(arr, left, right, k):
    """
    A function to find the k-th smallest element in the array using the quick_select algorithm.

    :param arr: List of elements
    :param left: The starting index of the sublist
    :param right: The ending index of the sublist
    :param k: The order of the element to find (zero-indexed)
    :return: The k-th smallest element of the list
    """
    if left == right:  # list has only one element?
        return arr[left]

    # Select a random pivot_index between left and right
    pivot_index = random.randint(left, right)

    # Get the index of the pivot element after partition
    pivot_index = partition(arr, left, right, pivot_index)

    # The pivot is in its final sorted position
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k)
    else:
        return quick_select(arr, pivot_index + 1, right, k)


def partition(arr, left, right, pivot_index):
    pivot_val = arr[pivot_index]
    # move pivot to end
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    
    # move all smaller elements to the left
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_val:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    # move pivot to its final place
    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index


# Example usage:
arr = [3, 1, 2, 5, 4]
k = 2  # Find the 3rd smallest element; k is zero-indexed so k = 2 represents the 3rd element
print("The k-th smallest element is:", quick_select(arr, 0, len(arr) - 1, k))

# TODO: add more tests