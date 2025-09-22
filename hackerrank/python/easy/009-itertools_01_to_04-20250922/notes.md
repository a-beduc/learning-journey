## list comprehension vs map()

We could be tempted to use map() instead of list comprehension but if
i believe the comment on this stack overflow question, list comprehension
are more efficient. And they are more easily read most of the time.

link: https://stackoverflow.com/questions/1247486/list-comprehension-vs-map


## flatten lists


* Transform `[[A, B], [C, D, E]]`
* into `[A, B, C, D, E]`

snippet:
```
[item for sublist in list_combined for item in sublist]
```

## idea : sort input before processing (for 4)