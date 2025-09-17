#!/bin/bash

# Cut 3
input=$(cat)
echo "$input" | cut -b 2-7

# Cut 4
input=$(cat)
echo "$input" | cut -c 1-4

# Cut 5
input=$(cat)
echo "$input" | cut -f 1-3

# Cut 6
input=$(cat)
echo "$input" | cut -c 13-

# Cut 7
input=$(cat)
echo "$input" | cut -d " " -f 4

# Cut 8
input=$(cat)
echo "$input" | cut -d ' ' -f 1-3

# Cut 9
input=$(cat)
echo "$input" | cut -f 2-
