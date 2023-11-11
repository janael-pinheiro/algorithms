package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInsertionSort(t *testing.T) {
	for _, test := range testValues {
		sortedValues := insertionSort(test.input)
		assert.Equal(t, test.expectedOutput, sortedValues)
	}
}
