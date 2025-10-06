#!/bin/bash

# 01
awk 'NF != 4 {
    print "Not all scores are available for", $1;
}'

# 02
awk '{
if ( $2 >= 50 && $3 >= 50 && $4 >= 50 )
    print $1, ": Pass";
else
    print $1, ": Fail";
}'

# 03
awk '{
    total = $2 + $3 + $4;
    average = total / 3;
    if ( average >= 80 )
        print $0, ": A";
    else if ( average >= 60 )
        print $0, ": B";
    else if ( average >= 50 )
        print $0, ": C";
    else
        print $0, ": FAIL";
}'

# 04
awk 'ORS = NR % 2 ? ";" : "\n"'
