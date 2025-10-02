## 012 The captain's room
Three solutions for the exercise 12 "The captain room"

* 01 naive approach (My 1st solution)
  * easy
* 02 counter approach (Second solution)
  * easy
* 03 mathematics approach (Found online)
  * ``k``: number of member per group
  * ``S``: Sum of room numbers (sum input)
  * ``U``: Sum of unique room numbers (sum set input) (remove duplicate)
  * Each group contribute ``k``, except captain contribute ``1``
  * `(k * U - S) / (k - 1) = captain`

* example:
  * `k = 3`
  * ``input = 1 1 1 2 2 2 3 3 3 4 4 4 13``
  * ``S = 3 + 6 + 9 + 12 + 13 = 43``
  * ``U = 1 + 2 + 3 + 4 + 13 = 23``
  * ``k * U = 69``
  * ``k * U - S = 26``
  * ``(k * U - S) / (k - 1) = 13``
  * captain = ``13``
