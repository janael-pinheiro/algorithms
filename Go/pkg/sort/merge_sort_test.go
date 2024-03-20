package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMergeSort(t *testing.T) {
	for _, test := range testValues {
		sortedValues := mergeSort(test.input, 0, len(test.input)-1)
		assert.Equal(t, test.expectedOutput, sortedValues)
	}
}
