#!/bin/bash
read X
read Y
read Z

if [ $X -eq $Y ] && [ $X -eq $Z ]; then
    echo "EQUILATERAL"
elif [ $X -ne $Y ] && [ $X -ne $Z ] && [ $Y -ne $Z ]; then
    echo "SCALENE"
else
    echo "ISOSCELES"
fi
