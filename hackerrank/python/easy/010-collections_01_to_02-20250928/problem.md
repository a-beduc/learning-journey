## 01 collections.Counter()
https://www.hackerrank.com/challenges/collections-counter/problem

collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Sample Code
```
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
```
Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

Constraints

* `0 < X < 10^3`
* `0 < N < 10^3`
* `20 < xi < 100`
* `2 < shoe size < 20`

Output Format

Print the amount of money earned by Raghu.

Sample Input
```
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
```
Sample Output
```
200
```
Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned = 55 + 45 + 40 +60 = $200

## 02 DefaultDict Tutorial
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

The defaultdict tool is a container in the collections class of Python. 
It's similar to the usual dictionary (dict) container, but the only difference 
is that a defaultdict will have a default value if that key has not been set 
yet. If you didn't use a defaultdict you'd have to check to see if that key 
exists, and if it doesn't, set it to what you want.

For example:

```
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
```
This prints:
```
('python', ['awesome', 'language'])
('something-else', ['not relevant'])
```
In this challenge, you will be given 2 integers, n and m. There are n words, 
which might repeat, in word group A. There are m words belonging to word group 
B. For each m words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of m in group A. If it does not appear, 
print -1.

Example

Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions 1 and 3 in group A.
The second word, 'c', does not appear in group A, so print -1.

Expected output:
```
1 3
-1
```
Input Format

The first line contains integers, n and m separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.

Constraints

* `1 <= n <= 10000`
* `1 <= m <= 100`
* `1 <= lenght of each word in the input <= 100`

Output Format

Output m lines.
The I line should contain the 1-indexed positions of the occurrences of the I word separated by spaces.

Sample Input
```
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
```
Sample Output
```
1 2 4
3 5
```
Explanation

'a' appeared 3 times in positions 1, 2 and 4.
'b' appeared 2 times in positions 3 and 5.
In the sample problem, if 'c' also appeared in word group B, you would print -1.
