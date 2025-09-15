#!/bin/bash
read EXPRESSION
value=$(echo "scale=4; x=$EXPRESSION; if (x>0) x+=0.0005 else x-=0.0005; x" | bc -l)
echo "$value" | sed 's/.$//'
