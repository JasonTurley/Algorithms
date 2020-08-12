

def bubble_sort(A):
	N = len(A)
	for i in range(1, N):
		for j in range(0, N - 1):
			if A[j] > A[j + 1]:
				A[j], A[j + 1] = A[j + 1], A[j]

	return A

B = [7, 1, 3, 4, 0, 10, 9, 8]
print("List before sorting:", B)

B = bubble_sort(B)

print("List after sorting:", B)

