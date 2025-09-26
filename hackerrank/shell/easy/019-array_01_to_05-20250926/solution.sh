#!/bin/bash

# 01
mapfile -t countries
printf '%s ' "${countries[@]}"

# 02
mapfile -t countries
printf '%s ' "${countries[@]:3:5}"


# 03
mapfile -t countries
concatenate=()
for ((i=0; i<3; i++)); do
    concatenate+=("${countries[@]}")
done
printf '%s ' "${concatenate[@]}"

# 04
mapfile -t countries
printf '%s' "${countries[3]}"

# 05
#!/bin/bash
mapfile -t countries
echo ${#countries[@]}
