package org.example;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class SelectionSortTest {
    SelectionSort selectionSort;

    List<Integer> values;
    List<Integer> expected;

    @BeforeEach
    void setup(){
        this.selectionSort = new SelectionSort();
        this.values = Arrays.asList(10, 3, 8, 12, 4);
        this.expected  = Arrays.asList(3, 4, 8, 10, 12);
    }

    @Test
    void testSort(){
        List<Integer> sorted = selectionSort.sort(values);
        Assertions.assertArrayEquals(expected.toArray(), sorted.toArray());
    }

}
