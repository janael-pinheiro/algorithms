package sort

const FIRST_INDEX = 0

func bubleSort(values []int) []int {
	sorted_values := make([]int, 0)
	sorted_values = append(sorted_values, values...)
	has_changed := false
	array_length := len(sorted_values) - 1
	for ; array_length > FIRST_INDEX; array_length-- {
		for index := FIRST_INDEX; index < array_length; index++ {
			if sorted_values[index] > sorted_values[index+1] {
				temp := sorted_values[index]
				sorted_values[index] = sorted_values[index+1]
				sorted_values[index+1] = temp
				has_changed = true
			}
		}
		if !has_changed {
			break
		}
		has_changed = true
	}
	return sorted_values
}
