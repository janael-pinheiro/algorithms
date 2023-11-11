package sort

func insertionSort(valuesToSort []int) []int {
	n := len(valuesToSort)
	internalValueToSort := make([]int, n)
	copy(internalValueToSort, valuesToSort)
	for i := 1; i < n; i++ {
		j := i - 1
		value := internalValueToSort[i]
		for j >= 0 && internalValueToSort[j] > value {
			internalValueToSort[j+1] = internalValueToSort[j]
			j = j - 1
		}
		internalValueToSort[j+1] = value
	}
	return internalValueToSort
}
