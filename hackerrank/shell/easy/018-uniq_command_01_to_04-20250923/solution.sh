#!/bin/bash

# 01
uniq

# 02
uniq -c | sed 's/^ *//'

# 03
# ignore case
uniq -ci | sed 's/^ *//'

# 04
# only non repeated
uniq -u
