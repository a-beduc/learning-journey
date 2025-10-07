#!/bin/bash
mapfile -t countries
printf "%s\n" "${countries[@]}" | awk '!/[aA]/'
