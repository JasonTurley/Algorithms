"""
Implementation of the linear search algorithm:
	Checks every element in the list from beginning to end, only stopping once
	the target element is found, or when the entire list has been searched.

	Worst Case: O(n) when target is last element in list

For doctests run:
	python3 -m doctest -v linear_search.py

For manual testing run:
	python3 linear_search.py
"""

def linear_search(arr, x):
	"""Implementation of linear search in Python

	:param arr: a list of items (unsorted or sorted)
	:param x: the target value to search for
	:return: Index of the value if found, or None if not found

	Examples:
	>>> linear_search([10, 20, 30, 40, 50], 30)
	2

	>>> linear_search([10, 20, 30, 40, 50], 10)
	0

	>>> linear_search([10, 20, 30, 40, 50], 50)
	4

	>>> linear_search([10, 20, 30, 40, 50], 0)


	"""
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return None


if __name__ == "__main__":
	user_input = input("Enter numbers separated by spaces:\n")
	arr = [int(item) for item in user_input.split()]

	target = int(input("Enter the target value to search for:\n"))
	retval = linear_search(arr, target)

	if retval is not None:
		print(f"Found {target} at index {retval}")
	else:
		print(f"{target} not found")
