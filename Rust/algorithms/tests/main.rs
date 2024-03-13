use algorithms::sort;

#[test]
fn test_selection_sort() {
    let expected_values: [i32; 5] = [0, 2, 5, 6, 9];
    let mut values: [i32; 5] = [5, 6, 9, 2, 0];
    sort(&mut values);
    assert_eq!(values, expected_values);
}