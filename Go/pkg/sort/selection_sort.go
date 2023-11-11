package sort

func selectionSort(valuesToSort []int) []int {
	n := len(valuesToSort)

	for i := 0; i < n-1; i++ {
		minimum_index := i
		for j := i + 1; j < n; j++ {
			if valuesToSort[j] < valuesToSort[minimum_index] {
				minimum_index = j
			}
		}

		temp := valuesToSort[minimum_index]
		valuesToSort[minimum_index] = valuesToSort[i]
		valuesToSort[i] = temp
	}
	return valuesToSort
}
