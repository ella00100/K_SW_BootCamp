import random

def quickSort2(arr, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = arr[(low + high) // 2]
	while low <= high :
		while arr[low] < pivot :
			low += 1
		while arr[high] > pivot :
			high -= 1
		if low <= high :
			arr[low], arr[high] = arr[high], arr[low]
			low, high = low + 1, high - 1

	mid = low

	quickSort2(arr, start, mid - 1)
	quickSort2(arr, mid, end)


dataAry = [random.randint(0,100) for _ in range(10)]


print('정렬 전 -->', dataAry)
quickSort2(dataAry,0,len(dataAry)-1)
print('정렬 후 -->', dataAry)