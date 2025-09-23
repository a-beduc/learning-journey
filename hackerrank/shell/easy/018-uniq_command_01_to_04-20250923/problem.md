## uniq command 01
https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-1/problem
In this challenge, we practice using the uniq command to eliminate consecutive repetitions of a line when a text file is piped through it.

Given a text file, remove the consecutive repetitions of any line.

Sample Input
```
00
00
01
01
00
00
02
02
```
Sample Output
```
00
01
00
02  
```

## uniq command 02
https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-2/problem

In this challenge, we practice using the uniq command to eliminate consecutive repetitions of a line when a text file is piped through it.

Given a text file, count the number of times each line repeats itself. Only consider consecutive repetitions. Display the space separated count and line, respectively. There shouldn't be any leading or trailing spaces. Please note that the uniq -c command by itself will generate the output in a different format than the one expected here.

Sample Output

Explanation

Sample Input
```
00
00
01
01
00
00
02
02
03
aa
aa
aa
```
Sample Output
```
2 00
2 01
2 00
2 02
1 03
3 aa 
```
Explanation
```
00 is repeated twice
01 is repeated twice
00 is repeated twice
02 is repeated twice
03 occurs once
aa is repeated thrice  
```

## uniq command 03
https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-3/problem

Given a text file, count the number of times each line repeats itself (only consider consecutive repetions). Display the count and the line, separated by a space. There shouldn't be leading or trailing spaces. Please note that the uniq -c command by itself will generate the output in a different format.

This time, compare consecutive lines in a case insensitive manner. So, if a line X is followed by case variants, the output should count all of them as the same (but display only the form X in the second column).

So, as you might observe in the case below: aa, AA and Aa are all counted as instances of 'aa'.

Sample Input
```
00
00
01
01
00
00
02
02
03
aa
AA
Aa
```
Sample Output
```
2 00
2 01
2 00
2 02
1 03
3 aa 
```
Explanation
```
00 is repeated twice
01 is repeated twice
00 is repeated twice
02 is repeated twice
03 occurs once
aa is repeated thrice (if we ignore case - AA, Aa are the same as 'aa')
```

## uniq command 04
https://www.hackerrank.com/challenges/text-processing-in-linux-the-uniq-command-4/problem
Given a text file, display only those lines which are not followed or preceded by identical replications.

Sample Input
```
A00
a00
01
01
00
00
02
02
A00
03
aa
aa
aa
```
Sample Output
```
A00
a00
A00
03
```
Explanation

The comparison is case sensitive, so the first instance of "A00" and "a00" are considered different, hence unique.
The next instance of A00 is succeeded and preceded by different lines, so that is also included in the output.
The same holds true for 03 - it is succeeded and preceded by different lines, so that is also included in the output. 
