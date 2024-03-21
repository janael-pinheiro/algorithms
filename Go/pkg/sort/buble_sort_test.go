package sort

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestBubleSort(t *testing.T) {
	for _, test := range testValues {
		sortedValues := bubleSort(test.input)
		assert.Equal(t, test.expectedOutput, sortedValues)
	}
}

func BenchmarkBubleSort(b *testing.B) {
	for n := 0; n < b.N; n++ {
		for _, test := range testValues {
			bubleSort(test.input)
		}
	}
}
