

def selection_sort(arr):

	all_arr = []
	temp = []
	for k in arr:
		temp.append(k)
	all_arr.append(temp)

	i = len(arr)-1

	while i>0:
		largest_idx = -1
		for j in range(i+1):
			if largest_idx == -1:
				largest_idx = j
			elif arr[j]>arr[largest_idx]:
				largest_idx = j

		temp = arr[i]
		arr[i] = arr[largest_idx]
		arr[largest_idx] = temp

		temp = []
		for k in arr:
			temp.append(k)
		all_arr.append(temp)

		i-=1


	return all_arr


selection_sort([400,300,200,100])