package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

type valuesToSort struct {
	input          []int
	expectedOutput []int
}

var testValues = []valuesToSort{
	{
		input:          []int{7, 9, 0, 48, 3, 87},
		expectedOutput: []int{0, 3, 7, 9, 48, 87},
	},
	{
		input:          []int{5, 10, 9, 3, 1},
		expectedOutput: []int{1, 3, 5, 9, 10},
	},
	{
		input:          []int{100, 50, 70, 3, 45, 0},
		expectedOutput: []int{0, 3, 45, 50, 70, 100},
	},
	{
		input:          []int{1, 4, 2, 3, 5},
		expectedOutput: []int{1, 2, 3, 4, 5},
	},
	{
		input:          []int{6, 7, 8, 9, 10},
		expectedOutput: []int{6, 7, 8, 9, 10},
	},
	{
		input:          []int{6, 7, 9, 9, 10},
		expectedOutput: []int{6, 7, 9, 9, 10},
	},
	{
		input:          []int{4, 3, 12, 1, 5, 5, 3, 9},
		expectedOutput: []int{1, 3, 3, 4, 5, 5, 9, 12},
	},
	{
		input:          []int{5, 4, 3, 2, 1},
		expectedOutput: []int{1, 2, 3, 4, 5},
	},
}

func TestSelectionSort(t *testing.T) {
	for _, test := range testValues {
		sortedValues := selectionSort(test.input)
		assert.Equal(t, test.expectedOutput, sortedValues)
	}

}
