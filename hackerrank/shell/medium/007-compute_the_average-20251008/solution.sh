#!/bin/bash
read -r N
mapfile -t numbers
total=0

for number in "${numbers[@]}"; do
    (( total += number ))
done

average=$(echo "$total / $N" | bc -l)
printf "%.3f" "$average"
