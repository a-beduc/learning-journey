intro 
https://www.thegeekstuff.com/2010/01/awk-introduction-tutorial-7-awk-print-examples/

variable
https://www.thegeekstuff.com/2010/01/awk-tutorial-understand-awk-variables-with-3-practical-examples/
* $0 store complete record
* \$1 - \$n store separate field of record

builtin
https://www.thegeekstuff.com/2010/01/8-powerful-awk-built-in-variables-fs-ofs-rs-ors-nr-nf-filename-fnr//
* FS: Field Separator (default space)
* OFS: Output Field Separator (default space)
* RS: Record Separator (default \n)
* ORS: Output Record Separator (default \n)
* NR: Number of Records (While processing, will store current line index)
* NF: Number of fields
* FILENAME: Store name of current input file (useful when processing multiple files at once)
* FNR: Number of record + Current input file, while processing will store current number of record).

operators
https://www.thegeekstuff.com/2010/02/unix-awk-operators/
* ~ (match pattern)

conditionals 
https://www.thegeekstuff.com/2010/02/awk-conditional-statements/

Syntax:
```
awk '/search pattern1/ {Actions}
     /search pattern2/ {Actions}' file
```
or 
```
awk -f script.awk file
```
or
```
awk 'BEGIN { actions; }
{ 
    if (conditionalA && conditionalB) 
        actions;
    else
        actions;
}
END { actions; }
' file
```
or (if conditional-expression true, action1 else action2)
```
awk 'conditional-expression ? action1 : action2' file
```