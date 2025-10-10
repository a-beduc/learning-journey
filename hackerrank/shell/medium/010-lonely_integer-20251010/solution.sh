#!/bin/bash
read -r N
read -r A
numbers=( $A )
printf "%s\n" "${numbers[@]}" | sort | uniq -u
