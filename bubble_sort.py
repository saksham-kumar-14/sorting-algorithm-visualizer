

def bubble_sort(arr):

	all_arr = []

	temp = []
	for i in arr:
		temp.append(i)
	all_arr.append(temp)

	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i] > arr[j]:
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp

			temp = []
			for k in arr:
				temp.append(k)
			all_arr.append(temp)

	return all_arr