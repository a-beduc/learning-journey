## sort command 01
https://www.hackerrank.com/challenges/text-processing-sort-1/problem
In this challenge, we practice using the sort command to sort input in text or TSV formats.

Given a text file, order the lines in lexicographical order.

Input Format

A text file.

Output Format

Output the text file with the lines reordered in lexicographical order.

Sample Input
```
Dr. Rajendra Prasad     January 26, 1950    May 13, 1962
Dr. S. Radhakrishnan        May 13, 1962    May 13, 1967
Dr. Zakir Hussain       May 13, 1967    August 24, 1969
Shri Varahagiri Venkata Giri        August 24, 1969 August 24, 1974
Shri Fakhruddin Ali Ahmed       August 24, 1974 February 11, 1977
Shri Neelam Sanjiva Reddy       July 25, 1977   July 25, 198
```
Sample Output
```
Dr. Rajendra Prasad     January 26, 1950    May 13, 1962
Dr. S. Radhakrishnan        May 13, 1962    May 13, 1967
Dr. Zakir Hussain       May 13, 1967    August 24, 1969
Shri Fakhruddin Ali Ahmed       August 24, 1974 February 11, 1977
Shri Neelam Sanjiva Reddy       July 25, 1977   July 25, 198
Shri Varahagiri Venkata Giri        August 24, 1969 August 24, 1974
```

## sort command 02
https://www.hackerrank.com/challenges/text-processing-sort-2/problem

In this challenge, we practice using the sort command to sort input in text or TSV formats.

Given a text file, order the lines in reverse lexicographical order (i.e. Z-A instead of A-Z).

Input Format

A text file.

Output Format

Output the text file with the lines reordered in reverse lexicographical order.

Sample Input
```
Dr. Rajendra Prasad     January 26, 1950    May 13, 1962
Dr. S. Radhakrishnan        May 13, 1962    May 13, 1967
Dr. Zakir Hussain       May 13, 1967    August 24, 1969
Shri Varahagiri Venkata Giri        August 24, 1969 August 24, 1974
Shri Fakhruddin Ali Ahmed       August 24, 1974 February 11, 1977
Shri Neelam Sanjiva Reddy       July 25, 1977   July 25, 198
```
Sample Output
```
Shri Varahagiri Venkata Giri        August 24, 1969 August 24, 1974
Shri Neelam Sanjiva Reddy       July 25, 1977   July 25, 198
Shri Fakhruddin Ali Ahmed       August 24, 1974 February 11, 1977
Dr. Zakir Hussain       May 13, 1967    August 24, 1969
Dr. S. Radhakrishnan        May 13, 1962    May 13, 1967
Dr. Rajendra Prasad     January 26, 1950    May 13, 1962
```

## sort command 03
https://www.hackerrank.com/challenges/text-processing-sort-3/problem

In this challenge, we practice using the sort command to sort input in text or TSV formats.

You are given a text file where each line contains a number. The numbers may be either an integer or have decimal places. There will be no extra characters other than the number or the newline at the end of each line. Sort the lines in ascending order - so that the first line holds the numerically smallest number, and the last line holds the numerically largest number.

Input Format

A text file where each line contains a positive number (less than 100) as described above.

Output Format

Output the text file with the lines reordered in numerically ascending order.

Sample Input
```
9.1
43.7
2.2
62.1
2.1
9.3
43.5
4.6
44.6
4.7
42.7
47.4
46.6
4.5
55.6
4
9.2
66.6
2
2.3
```
Sample Output
```
2
2.1
2.2
2.3
4
4.5
4.6
4.7
9.1
9.2
9.3
42.7
43.5
43.7
44.6
46.6
47.4
55.6
62.1
66.6
```

## sort command 04
https://www.hackerrank.com/challenges/text-processing-sort-4/problem

You are given a file of text, where each line contains a number (which may be either an integer or have decimal places). There will be no extra characters other than the number or the newline at the end of each line. Sort the lines in descending order - - such that the first line holds the (numerically) largest number and the last line holds the (numerically) smallest number.

Input Format

A text file where each line contains a number as described above.

Output Format

The text file, with lines re-ordered in descending order (numerically).

Sample Input
```
9.1
43.7
2.2
62.1
2.1
9.3
43.5
4.6
44.6
4.7
42.7
47.4
46.6
4.5
55.6
4
9.2
66.6
2
2.3
```
Sample Output
```
66.6
62.1
55.6
47.4
46.6
44.6
43.7
43.5
42.7
9.3
9.2
9.1
4.7
4.6
4.5
4
2.3
2.2
2.1
2
```

## sort command 05
https://www.hackerrank.com/challenges/text-processing-sort-5/problem

You are given a file of text,which contains temperature information about American cities, in TSV (tab-separated) format. The first column is the name of the city and the next four columns are the average temperature in the months of Jan, Feb, March and April (see the sample input). Rearrange the rows of the table in descending order of the values for the average temperature in January.

Input Format

A text file where each line contains a row of data as described above.

Output Format

Rearrange the rows of the table in descending order of the values for the average temperature in January (i.e, the mean temperature value provided in the second column).

Sample Input 0
```
Albany, N.Y.    22.2    46.6    71.1    49.3    38.60    136    64.4    57
Albuquerque, N.M.    35.7    55.6    78.5    57.3    9.47    60    11.0    64
Anchorage, Alaska    15.8    36.3    58.4    34.1    16.08    115    70.8    39 / 60
Asheville, N.C.    35.8    54.1    73.0    55.2    47.07    126    15.3    39
Atlanta, Ga.    42.7    61.6    80.0    62.8    50.20    115    2.1    69 / 65
Atlantic City, N.J.    32.1    50.6    75.3    55.1    40.59    113    16.2    60 / 54
Austin, Texas    50.2    68.3    84.2    70.6    33.65    85    0.9    62 / 58
Baltimore, Md.    32.3    53.2    76.5    55.4    41.94    115    21.5    53
Baton Rouge, La.    50.1    66.6    81.7    68.1    63.08    110    0.2    52 / 46
Billings, Mont.    24.0    46.1    72.0    48.1    14.77    96    56.9    69
Birmingham, Ala.    42.6    61.3    80.2    62.9    53.99    117    1.5    60
Bismarck, N.D.    10.2    43.3    70.4    45.2    16.84    96    44.3    64
Boise, Idaho    30.2    50.6    74.7    52.8    12.19    89    20.6    64
Boston, Mass.    29.3    48.3    73.9    54.1    42.53    127    42.8    52 / 66
Bridgeport, Conn.    29.9    48.9    74.0    54.7    44.15    119    26.2    55 / 49
```
Sample Output 0
```
Austin, Texas    50.2    68.3    84.2    70.6    33.65    85    0.9    62 / 58
Baton Rouge, La.    50.1    66.6    81.7    68.1    63.08    110    0.2    52 / 46
Atlanta, Ga.    42.7    61.6    80.0    62.8    50.20    115    2.1    69 / 65
Birmingham, Ala.    42.6    61.3    80.2    62.9    53.99    117    1.5    60
Asheville, N.C.    35.8    54.1    73.0    55.2    47.07    126    15.3    39
Albuquerque, N.M.    35.7    55.6    78.5    57.3    9.47    60    11.0    64
Baltimore, Md.    32.3    53.2    76.5    55.4    41.94    115    21.5    53
Atlantic City, N.J.    32.1    50.6    75.3    55.1    40.59    113    16.2    60 / 54
Boise, Idaho    30.2    50.6    74.7    52.8    12.19    89    20.6    64
Bridgeport, Conn.    29.9    48.9    74.0    54.7    44.15    119    26.2    55 / 49
Boston, Mass.    29.3    48.3    73.9    54.1    42.53    127    42.8    52 / 66
Billings, Mont.    24.0    46.1    72.0    48.1    14.77    96    56.9    69
Albany, N.Y.    22.2    46.6    71.1    49.3    38.60    136    64.4    57
Anchorage, Alaska    15.8    36.3    58.4    34.1    16.08    115    70.8    39 / 60
Bismarck, N.D.    10.2    43.3    70.4    45.2    16.84    96    44.3    64
```
Explanation 0

The data has been sorted in descending order of the average monthly temperature in January (i.e, the second column). 

## sort command 06
https://www.hackerrank.com/challenges/text-processing-sort-6/problem

You are given a file of tab separated weather data (TSV). There is no header column in this data file.
The first five columns of this data are: (a) the name of the city (b) the average monthly temperature in Jan (in Fahreneit). (c) the average monthly temperature in April (in Fahreneit). (d) the average monthly temperature in July (in Fahreneit). (e) the average monthly temperature in October (in Fahreneit).

You need to sort this file in ascending order of the second column (i.e. the average monthly temperature in January).

Input Format

A text file with multiple lines of tab separated data. The first five fields have been explained above

Output Format

Sort the data in ascending order of the average monthly temperature in January.

Sample Input
```
Albany, N.Y.    22.2    46.6    71.1    49.3    38.60   136 64.4    57
Albuquerque, N.M.   35.7    55.6    78.5    57.3    9.47    60  11.0    64
Anchorage, Alaska   15.8    36.3    58.4    34.1    16.08   115 70.8    39 / 60
Asheville, N.C. 35.8    54.1    73.0    55.2    47.07   126 15.3    39
Atlanta, Ga.    42.7    61.6    80.0    62.8    50.20   115 2.1 69 / 65
Atlantic City, N.J. 32.1    50.6    75.3    55.1    40.59   113 16.2    60 / 54
Austin, Texas   50.2    68.3    84.2    70.6    33.65   85  0.9 62 / 58
Baltimore, Md.  32.3    53.2    76.5    55.4    41.94   115 21.5    53
Baton Rouge, La.    50.1    66.6    81.7    68.1    63.08   110 0.2 52 / 46
Billings, Mont. 24.0    46.1    72.0    48.1    14.77   96  56.9    69
Birmingham, Ala.    42.6    61.3    80.2    62.9    53.99   117 1.5 60
Bismarck, N.D.  10.2    43.3    70.4    45.2    16.84   96  44.3    64
Boise, Idaho    30.2    50.6    74.7    52.8    12.19   89  20.6    64
Boston, Mass.   29.3    48.3    73.9    54.1    42.53   127 42.8    52 / 66
Bridgeport, Conn.   29.9    48.9    74.0    54.7    44.15   119 26.2    55 / 49
```
Sample Output
```
Bismarck, N.D.  10.2    43.3    70.4    45.2    16.84   96  44.3    64
Anchorage, Alaska   15.8    36.3    58.4    34.1    16.08   115 70.8    39 / 60
Albany, N.Y.    22.2    46.6    71.1    49.3    38.60   136 64.4    57
Billings, Mont. 24.0    46.1    72.0    48.1    14.77   96  56.9    69
Boston, Mass.   29.3    48.3    73.9    54.1    42.53   127 42.8    52 / 66
Bridgeport, Conn.   29.9    48.9    74.0    54.7    44.15   119 26.2    55 / 49
Boise, Idaho    30.2    50.6    74.7    52.8    12.19   89  20.6    64
Atlantic City, N.J. 32.1    50.6    75.3    55.1    40.59   113 16.2    60 / 54
Baltimore, Md.  32.3    53.2    76.5    55.4    41.94   115 21.5    53
Albuquerque, N.M.   35.7    55.6    78.5    57.3    9.47    60  11.0    64
Asheville, N.C. 35.8    54.1    73.0    55.2    47.07   126 15.3    39
Birmingham, Ala.    42.6    61.3    80.2    62.9    53.99   117 1.5 60
Atlanta, Ga.    42.7    61.6    80.0    62.8    50.20   115 2.1 69 / 65
Baton Rouge, La.    50.1    66.6    81.7    68.1    63.08   110 0.2 52 / 46
Austin, Texas   50.2    68.3    84.2    70.6    33.65   85  0.9 62 / 58
```
Explanation

The data has been sorted in ascending order of the average monthly temperature in January (i.e, the second column). 

## sort command 07
https://www.hackerrank.com/challenges/text-processing-sort-7/problem

You are given a file of pipe-delimited weather data (TSV). There is no header column in this data file. The first five columns of this data are: (a) the name of the city (b) the average monthly temperature in Jan (in Fahreneit). (c) the average monthly temperature in April (in Fahreneit). (d) the average monthly temperature in July (in Fahreneit). (e) the average monthly temperature in October (in Fahreneit).

You need to sort this file in descending order of the second column (i.e. the average monthly temperature in January).

Input Format

A text file with multiple lines of pipe-delimited data. The first five fields have been explained above

Output Format

Sort the data in descending order of the average monthly temperature in January.

Sample Input
```
Albany, N.Y.|22.2|46.6|71.1|49.3|38.60|136|64.4|57
Albuquerque, N.M.|35.7|55.6|78.5|57.3|9.47|60|11.0|64
Anchorage, Alaska|15.8|36.3|58.4|34.1|16.08|115|70.8|39 / 60
Asheville, N.C.|35.8|54.1|73.0|55.2|47.07|126|15.3|39
Atlanta, Ga.|42.7|61.6|80.0|62.8|50.20|115|2.1|69 / 65
Atlantic City, N.J.|32.1|50.6|75.3|55.1|40.59|113|16.2|60 / 54
Austin, Texas|50.2|68.3|84.2|70.6|33.65|85|0.9|62 / 58
Baltimore, Md.|32.3|53.2|76.5|55.4|41.94|115|21.5|53
Baton Rouge, La.|50.1|66.6|81.7|68.1|63.08|110|0.2|52 / 46
Billings, Mont.|24.0|46.1|72.0|48.1|14.77|96|56.9|69
Birmingham, Ala.|42.6|61.3|80.2|62.9|53.99|117|1.5|60
Bismarck, N.D.|10.2|43.3|70.4|45.2|16.84|96|44.3|64
Boise, Idaho|30.2|50.6|74.7|52.8|12.19|89|20.6|64
Boston, Mass.|29.3|48.3|73.9|54.1|42.53|127|42.8|52 / 66
Bridgeport, Conn.|29.9|48.9|74.0|54.7|44.15|119|26.2|55 / 49
```
Sample Output
```
Austin, Texas|50.2|68.3|84.2|70.6|33.65|85|0.9|62 / 58
Baton Rouge, La.|50.1|66.6|81.7|68.1|63.08|110|0.2|52 / 46
Atlanta, Ga.|42.7|61.6|80.0|62.8|50.20|115|2.1|69 / 65
Birmingham, Ala.|42.6|61.3|80.2|62.9|53.99|117|1.5|60
Asheville, N.C.|35.8|54.1|73.0|55.2|47.07|126|15.3|39
Albuquerque, N.M.|35.7|55.6|78.5|57.3|9.47|60|11.0|64
Baltimore, Md.|32.3|53.2|76.5|55.4|41.94|115|21.5|53
Atlantic City, N.J.|32.1|50.6|75.3|55.1|40.59|113|16.2|60 / 54
Boise, Idaho|30.2|50.6|74.7|52.8|12.19|89|20.6|64
Bridgeport, Conn.|29.9|48.9|74.0|54.7|44.15|119|26.2|55 / 49
Boston, Mass.|29.3|48.3|73.9|54.1|42.53|127|42.8|52 / 66
Billings, Mont.|24.0|46.1|72.0|48.1|14.77|96|56.9|69
Albany, N.Y.|22.2|46.6|71.1|49.3|38.60|136|64.4|57
Anchorage, Alaska|15.8|36.3|58.4|34.1|16.08|115|70.8|39 / 60
Bismarck, N.D.|10.2|43.3|70.4|45.2|16.84|96|44.3|64
```
Explanation

The data has been sorted in descending order of the average monthly temperature in January (i.e, the second column). 
