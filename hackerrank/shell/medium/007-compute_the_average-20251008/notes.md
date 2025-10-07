* for arithmetic operation use ``(( operation ))`` this is the modern way
```bash
# don't do this
for number in ${numbers[@]}; do
    let total+=$number
done
```
```bash
# this doesn't
for number in "${numbers[@]}"; do
    (( total += number ))
done
```

* use bc -l to process calculation with float
* printf expect args not data stream by default, hence not using pipe