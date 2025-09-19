#!/bin/bash

# 01
input=$(cat)
echo "$input" | tail -n 20

# 02
# careful with echo "$input" it can adds newlines, that will mess with bytes (-c)
# no need to buffer in a variable, it will read stdin directly
tail -c 20
