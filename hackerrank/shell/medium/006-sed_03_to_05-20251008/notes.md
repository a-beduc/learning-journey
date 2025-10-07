read this:
https://www.grymoire.com/Unix/Sed.html

sed use BRE (Basic Regular Expression) -> need to escape "\("
or use the -r flag to explicitly use RegEx
awk use ERE (Extended Regular Expression) -> no need to escape "("

the character after the 's' is the delimiter, it can be changed!


