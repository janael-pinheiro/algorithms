package sort

import "slices"

func countingSort(values []int) []int {
	length := len(values)
	maximum := slices.Max(values)
	count_array := make([]int, maximum+1)
	for i := 0; i < length; i++ {
		count_array[values[i]] += 1
	}

	for j := 1; j < maximum+1; j++ {
		count_array[j] += count_array[j-1]
	}

	output_array := make([]int, length)
	k := length - 1
	for ; k >= 0; k-- {
		output_array[count_array[values[k]]-1] = values[k]
		count_array[values[k]] -= 1
	}
	return output_array
}
