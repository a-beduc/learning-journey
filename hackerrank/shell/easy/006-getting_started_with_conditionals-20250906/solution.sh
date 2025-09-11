#!/bin/bash
read IN
IN=$(echo "$IN" | tr 'a-z' 'A-Z')

if [ "$IN" = "Y" ]; then
    echo "YES"
elif [ "$IN" = "N" ]; then
    echo "NO"
fi
