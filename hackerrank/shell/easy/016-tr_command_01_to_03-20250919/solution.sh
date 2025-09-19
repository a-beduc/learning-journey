#!/bin/bash

# 01
tr '()' '[]'

# 02
# delete -d
tr -d [a-z]

# 03
# squeeze repetitive character -s
tr -s " "
