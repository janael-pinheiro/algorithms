package org.example;

import java.util.ArrayList;
import java.util.List;

public class InsertionSort {
    public List<Integer> sort(List<Integer> valuesToSort) {
        int n = valuesToSort.size();
        List<Integer> internalValuesToSort = new ArrayList<>(valuesToSort);
        for (int i = 1; i < n; i++) {
            int j = i - 1;
            int value = internalValuesToSort.get(i);
            while (j >= 0 && internalValuesToSort.get(j) > value) {
                internalValuesToSort.set(j + 1, internalValuesToSort.get(j));
                j--;
            }
            internalValuesToSort.set(j + 1, value);
        }
        return internalValuesToSort;
    }
}
