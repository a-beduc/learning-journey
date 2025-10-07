#!/bin/bash
mapfile -t countries
printf "%s\n" "${countries[@]}" | sed 's/^[A-Z]/\./' | tr '\n' ' '
