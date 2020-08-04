"""
Implementation of the insertion sort algorithm:


For doctests run:
	python3 -m doctest -v insertion_sort.py

For manual testing run:
	python3 insertion_sort.py
"""

def insertion_sort(arr):
	"""Implememtation of insertion sort in Python

	:param arr: a list of numbers (unsorted or sorted)
	:return: the sorted array

	Examples:
	>>> insertion_sort([7, 4, 2, 8, 5])
	[2, 4, 5, 7, 8]

	>>> insertion_sort([1, 12, 5, 9, 15, 4])
	[1, 4, 5, 9, 12, 15]

	>>> insertion_sort([2, 4, 6, 8, 10])
	[2, 4, 6, 8, 10]

	>>> insertion_sort([])
	[]

	"""

	for i in range(1, len(arr)):
		j = i - 1
		key = arr[i]

		# move numbers greater than key to one position up
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1

		arr[j + 1] = key

	return arr

if __name__ == "__main__":
	user_input = input("Enter numbers separated by spaces:\n")
	arr = [int(item) for item in user_input.split()]

	arr = insertion_sort(arr)

	print("Here is the sorted list:")
	print(arr)
