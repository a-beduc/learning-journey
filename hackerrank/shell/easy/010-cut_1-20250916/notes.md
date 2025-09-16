### echo
the quotes are needed in the pipeline otherwise echo will
get rid of the '\n' newlines and throw back a single line.

```input
data written
on multiples
lines
```

echo $input 
    >>> data written on multiples lines
echo "$input" 
    >>> data written
    >>> on multiples
    >>> lines

### cut
cut -b <index> to cut a specific byte (see string as an array)
