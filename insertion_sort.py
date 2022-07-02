

def insertion_sort(arr):

	all_arr = []
	temp = []
	for i in arr:
		temp.append(i)
	all_arr.append(temp)

	for i in range(1,len(arr)):
		sub_arr = arr[:i]

		result_sub_arr = []
		inserted = False
		for j in range(len(sub_arr)):
			if not inserted and arr[i]<sub_arr[j]:
				result_sub_arr.append(arr[i])
				inserted = True
			result_sub_arr.append(sub_arr[j])
		if not inserted:
			result_sub_arr.append(arr[i])

		arr = result_sub_arr + arr[i+1:]
		temp = []
		for i in arr:
			temp.append(i)
		all_arr.append(temp)


	return all_arr
