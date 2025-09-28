## list comprehension vs map()

We could be tempted to use map() instead of list comprehension but if
i believe the comment on this stack overflow question, list comprehension
are more efficient. And they are more easily read most of the time.

link: https://stackoverflow.com/questions/1247486/list-comprehension-vs-map

/!\/!\/!\
2025-09-28 update: I just read that the difference between map and list comprehension is that
map is lazy, meaning that if we do not need to reference to the list element (one traversal), 
map might be the better approach.
/!\/!\/!\

## flatten lists


* Transform `[[A, B], [C, D, E]]`
* into `[A, B, C, D, E]`

snippet:
```
[item for sublist in list_combined for item in sublist]
```

## idea : sort input before processing (for 4)