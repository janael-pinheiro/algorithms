package org.example;

import java.util.List;

public class SelectionSort {
    public List<Integer> sort(List<Integer> valuesToSort) {
        int n = valuesToSort.size();
        for (int i=1; i < n; i++){
            int j = i - 1;
            int value = valuesToSort.get(i);
            while (j>=0 && valuesToSort.get(j) > value){
                valuesToSort.set(j+1, valuesToSort.get(j));
                j--;
            }
            valuesToSort.set(j+1, value);
        }
        return valuesToSort;
    }
}
