"""
Implementation of the binary search algorithm:
	Searches a sorted array for a target value. Splits the array in half on each
	search.

	Runs in O(log(n))

For doctests run:
	python3 -m doctest -v binary_search.py

For manual testing run:
	python3 binary_search.py
"""

def binary_search(arr, x):
	"""Implementation for binary search in Python

	:param arr: the sorted array to search
	:param x: the target value to search for
	:return: index of target value if found, or None if not found

	Examples:
	>>> binary_search([10, 20, 30, 40, 50, 60, 70, 80], 30)
	2

	>>> binary_search([10, 20, 30, 40, 50, 60, 70, 80], 80)
	7

	>>> binary_search([10, 20, 30, 40, 50, 60, 70, 80], 50)
	4

	>>> binary_search([10, 20, 30, 40, 50, 60, 70, 80], 100)

	"""
	return binary_search_helper(arr, x, 0, len(arr) - 1)


def binary_search_helper(arr, x, low, high):
	if low > high:
		return None

	mid = int( (low + high) / 2 )

	# target value is in left (lower) half
	if x < arr[mid]:
		return binary_search_helper(arr, x, low, mid - 1)

	# target value is in right (upper) half
	if x > arr[mid]:
		return binary_search_helper(arr, x, mid + 1, high)

	# found the target value
	if x == arr[mid]:
		return mid

if __name__ == "__main__":
	result = binary_search([10, 20, 30, 40, 50, 60, 70, 80], 30)

	if result is not None:
		print(f"Found at {result}")
	else:
		print("Not found")
