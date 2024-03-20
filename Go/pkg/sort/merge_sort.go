package sort

func mergeSort(values []int, left int, right int) []int {
	if left == right {
		return []int{values[left]}
	}

	var middle int = (left + right) / 2
	left_array := mergeSort(values, left, middle)
	right_array := mergeSort(values, middle+1, right)

	return marge_two_arrays(left_array, right_array)
}

func marge_two_arrays(left_array, right_array []int) []int {
	sorted_array := make([]int, 0)
	var i, j int
	for i < len(left_array) && j < len(right_array) {
		if left_array[i] < right_array[j] {
			sorted_array = append(sorted_array, left_array[i])
			i += 1
		} else {
			sorted_array = append(sorted_array, right_array[j])
			j += 1
		}
	}

	if i == len(left_array) {
		sorted_array = append(sorted_array, right_array[j:]...)
	}

	if j == len(right_array) {
		sorted_array = append(sorted_array, left_array[i:]...)
	}
	return sorted_array
}
