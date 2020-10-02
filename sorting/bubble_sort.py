"""
Implementation for the bubble sort alogithm:


For doctests run:
    python3 -m doctest -v bubble_sort.py

For manual testing run:
    python3 bubble_sort.py
"""

def bubble_sort(A):
    """
    :param arr: a list of numbers (unsorted or sorted)
    :return: the sorted array

    Examples:
    >>> bubble_sort([7, 1, 3, 4, 0])
    [0, 1, 3, 4, 7]

    >>> bubble_sort([12, 8, 10, 7, 1, 6])
    [1, 6, 7, 8, 10, 12]

    >>> bubble_sort([])
    []

    """
    N = len(A)
    for i in range(1, N):
	    for j in range(0, N - 1):
            # swap if current value is larger than the next value
		    if A[j] > A[j + 1]:
			    A[j], A[j + 1] = A[j + 1], A[j]

    return A


if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces:\n")
    nums = [int(item) for item in user_input.split()]

    nums = bubble_sort(nums)

    print("Here is the sorted list:")
    print(nums)
