package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSelectionSort(t *testing.T) {
	for _, test := range testValues {
		sortedValues := selectionSort(test.input)
		assert.Equal(t, test.expectedOutput, sortedValues)
	}

}
