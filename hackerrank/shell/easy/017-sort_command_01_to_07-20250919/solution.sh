#!/bin/bash

# 01
sort

# 02
sort -r

# 03
sort -n

# 04
sort -nr

# 05
# by default, sort separate column by blanks (space/tab)
# needs to force separation only for tabulation with ` -t $'\t' `
sort -t $'\t' -nr -k2

# 06
sort -t $'\t' -n -k2

# 07
sort -t '|' -nr -k2
