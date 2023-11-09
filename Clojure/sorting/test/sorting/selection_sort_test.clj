(ns sorting.selection-sort-test
  (:require [clojure.test :refer :all]
            [sorting.selection-sort :refer :all]))


(deftest test-recursive-selection
  (testing "should return the lowest value")
  (def test-values '(7, 2, 4, 78, 45, 0))
  (def input-test (map vector (range (count test-values)) test-values))
  (def expected '(5, 0))
  (is (= expected (recursive-selection input-test)))
  )

(deftest test-sort-values
  (testing "should return sorted values")
  (def test-values '(7, 2, 4, 78, 45, 0))
  (def input-test (map vector (range (count test-values)) test-values))
  (def expected '(0, 2, 4, 7, 45, 78))
  (is (= expected (sort-values input-test)))
  )