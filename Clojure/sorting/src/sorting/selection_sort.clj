(ns sorting.selection-sort)

(defn recursive-selection [values]
  (def filtered-values (filter #(< (nth % 1) (nth (nth values 0) 1)) values))
  (if (= (count filtered-values) 1)
    (nth filtered-values 0)
    (if (= (count filtered-values) 0)
      (nth values 0)
      (recur filtered-values)
    )))

(defn sort-values
  ([values]
   (sort-values (filter #(not= (nth % 0) (nth (recursive-selection values) 0)) values) (vector (nth (recursive-selection values) 1))  ))
  ([values sorted-values]
    (if (= (count values) 1)
    (conj sorted-values (nth (nth values 0) 1))
    (recur (filter #(not= (nth % 0) (nth (recursive-selection values) 0)) values) (conj sorted-values (nth (recursive-selection values) 1))))))