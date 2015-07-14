(defn parse-number
  [s]
  (if (re-find #"^-?\d+\.?\d*$" s)
    (read-string s)))

(def threads
  (slurp "results_threads.txt"))
(def raw
  (slurp "results_raw.txt"))
(def async
  (slurp "results_async.txt"))

(defn calculate-average [file]
  (-> file
      (clojure.string/split #"\n")
      (#(map parse-number %))
      (#(reduce + %))
      (/ 100)))

(println "Threads:" (str (calculate-average threads) "s"))
(println "Raw:" (str (calculate-average raw) "s"))
(println "Async:" (str (calculate-average async) "s"))
