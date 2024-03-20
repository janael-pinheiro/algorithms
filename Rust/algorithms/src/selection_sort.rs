pub fn sort(values_to_sort: &mut [i32]) {
    let n = values_to_sort.len();
    let mut i = 0;

    while i < n - 1 {
        let mut minimum_index = i;
        let mut j = i;
        while j < n {
            if values_to_sort[j] < values_to_sort[minimum_index] {
                minimum_index = j;
            }
            j += 1;
        }
        let temp = values_to_sort[minimum_index];
        values_to_sort[minimum_index] = values_to_sort[i];
        values_to_sort[i] = temp;
        i += 1;
    }
}
