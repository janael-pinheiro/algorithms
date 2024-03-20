package sort

func quickSort(values []int, left int, right int) []int {
	i := left
	j := right
	pivot := values[left]

	for i <= j {
		for values[i] < pivot {
			i += 1
		}
		for values[j] > pivot {
			j -= 1
		}
		if i <= j {
			temp := values[i]
			values[i] = values[j]
			values[j] = temp
			i += 1
			j -= 1
		}
	}
	if left < j {
		quickSort(values, left, j)
	}
	if i < right {
		quickSort(values, i, right)
	}
	return values
}
