# For the minion games.

* Iterate through word `W`
  * Check if letter `l` is vowel or consonant
    * If `l` vowel, add `len(W) - idx l` to participant 1
    * If `l` consonant, add `len(W) - idx l` to participant 2
  * Compare scores, print result.

## Why ?

The possible combinations for a word like BANANA 

from the B
* B, BA, BAN, BANA, BANAN, BANANA
* This is equal to length of word BANANA minus the index of the B (0) = 6


From the first N
* N, NA, NAN, NANA
* This is equal to length of word BANANA minus the index of the N (2) = 6 - 2 = 4