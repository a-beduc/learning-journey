https://www.thegeekstuff.com/2010/06/bash-array-tutorial/

## 01
Initializing an array during declaration

```#! /bin/bash
$cat arraymanip.sh
declare -a Unix=('Debian' 'Red hat' 'Red hat' 'Suse' 'Fedora');
```

Print the Whole Bash Array (separated by space),
If the index number is @ or *, all members of an array are referenced.
```#! /bin/bash
echo ${Unix[@]}
```
-----
The solution found up are old, a better way to read stdin in an array is to use
*mapfile* because of [SC2207](https://github.com/koalaman/shellcheck/wiki/SC2207)
```
# For bash 4.4+, must not be in posix mode, may use temporary files
mapfile -t array < <(mycommand)
```

*printf* seems more reliable to print out proper formatting

## 02

Extraction by offset and length for an array : `${array[@]:offset:length}`
```
$cat arraymanip.sh
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
echo ${Unix[@]:3:2}

$./arraymanip.sh
Suse Fedora
```

## 03
Concatenation of two Bash Arrays
```
Unix=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora' 'UTS' 'OpenLinux');
Shell=('bash' 'csh' 'jsh' 'rsh' 'ksh' 'rc' 'tcsh');

UnixShell=("${Unix[@]}" "${Shell[@]}")
```

Modern syntax
https://stackoverflow.com/questions/31143874/how-to-concatenate-arrays-in-bash

countries+=( "${countries[@]}" "${countries[@]}" )

## 05
We can get the length of an array using the special parameter called $#.

${#arrayname[@]} gives you the length of the array.
```
$ cat arraymanip.sh
declare -a Unix=('Debian' 'Red hat' 'Suse' 'Fedora');
echo ${#Unix[@]}    #Number of elements in the array
echo ${#Unix}       #Number of characters in the first element of the array.i.e Debian
echo ${#Unix[3]}    #Number of characters in the element at index 3 of the array.i.e Suse
$./arraymanip.sh
4
6
4
```