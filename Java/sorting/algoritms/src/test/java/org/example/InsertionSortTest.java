package org.example;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class InsertionSortTest {

    InsertionSort sorting;

    List<Integer> values;

    List<Integer> expected;

    @BeforeEach
    void setup(){
        this.sorting = new InsertionSort();
        this.values = Arrays.asList(10, 3, 8, 12, 4);
        this.expected  = Arrays.asList(3, 4, 8, 10, 12);

    }

    @Test
    void testSort(){
        List<Integer> sorted = sorting.sort(this.values);
        Assertions.assertArrayEquals(this.expected.toArray(), sorted.toArray());
    }

    @Test
    void testSortWithNegativeValues(){
        this.values = Arrays.asList(10, -4, 3, -8, 12, 4, 1000, 0);
        this.expected = Arrays.asList(-8, -4, 0, 3, 4, 10, 12, 1000);
        List<Integer> sorted = sorting.sort(values);
        Assertions.assertArrayEquals(this.expected.toArray(), sorted.toArray());
    }
}
