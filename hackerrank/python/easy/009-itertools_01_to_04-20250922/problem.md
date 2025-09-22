## 01 itertools.product()
https://www.hackerrank.com/challenges/itertools-product/problem

This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

Sample Code
```
>>> from itertools import product
>>>
>>> print list(product([1,2,3],repeat = 2))
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
>>>
>>> print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
>>>
>>> A = [[1,2,3],[3,4,5]]
>>> print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
>>>
>>> B = [[1,2,3],[3,4,5],[7,8]]
>>> print list(product(*B))
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]
```
Task

You are given a two lists A and B. Your task is to compute their cartesian product AXB.

Example
```
A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
```
Note:
A and B are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

Constraints
```
0 < A < 30
0 < B < 30
```

Output Format

Output the space separated tuples of the cartesian product.

Sample Input
```
1 2
3 4
```
Sample Output
```
(1, 3) (1, 4) (2, 3) (2, 4)
```

## 02 itertools.permutations()
https://www.hackerrank.com/challenges/itertools-permutations/problem

This tool returns successive r length permutations of elements in an iterable.

If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

Sample Code
```
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```
Task

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string S and the integer value k.

Constraints

* `0 < k <= len(S)`

The string contains only UPPERCASE characters.

Output Format

Print the permutations of the string S on separate lines.

Sample Input
```
HACK 2
```
Sample Output
```
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
```
Explanation

All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.

## 03 itertools.combinations()
https://www.hackerrank.com/challenges/itertools-combinations/problem

This tool returns the r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code
```
>>> from itertools import combinations
>>> 
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```
Task

You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints
* `0 < k <= len(S)`

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines.

Sample Input
```
HACK 2
```
Sample Output
```
A
C
H
K
AC
AH
AK
CH
CK
HK
```


## 04 itertools.combinations_with_replacement()
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
This tool returns r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

```
>>> from itertools import combinations_with_replacement
>>> 
>>> print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
>>> 
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]
```
Task

You are given a string S.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value k separated by a space.

Constraints

* `0 < k <= len(S)`

The string contains only UPPERCASE characters.

Output Format

Print the combinations with their replacements of string S on separate lines.

Sample Input
```
HACK 2
```
Sample Output
```
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
```