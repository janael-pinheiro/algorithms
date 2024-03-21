package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountingSort(t *testing.T) {
	for _, test := range testValues {
		sortedValues := countingSort(test.input)
		assert.Equal(t, test.expectedOutput, sortedValues)
	}
}

func BenchmarkCountingSort(b *testing.B) {
	for n := 0; n < b.N; n++ {
		for _, test := range testValues {
			countingSort(test.input)
		}
	}
}
