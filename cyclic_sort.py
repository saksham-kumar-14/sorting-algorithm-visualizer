
# specifically designed for the array to be given by interface.py
def cyclic_sort(arr):
	all_arr = []

	temp = []
	for i in arr:
		temp.append(i)
	all_arr.append(temp)

	i =0 
	while i<len(arr):
		correctIdx = (arr[i]-100)//50
		if i!=correctIdx:
			temp = arr[correctIdx]
			arr[correctIdx] = arr[i]
			arr[i] = temp
		else:
			i+=1

		temp = []
		for j in arr:
			temp.append(j)
		all_arr.append(temp)


	return all_arr