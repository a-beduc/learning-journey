## 03 collections.namedtuple()

lightweight containers, create containers that can be accessed with name (like a dict) or with index (like a tuple)
arguments are positional, none can be optional it seems.
Might be lighter solution than dataclasses to create DTO.
```
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11
```
```
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y
```

## 04 collections.OrderedDict()
Since python 3.7 normal dict keep order of insertion. This class is not needed
anymore. (I still used it for the solution tho).

## 05 

https://docs.python.org/3/library/collections.html#collections.deque

"deck", double-end queue, not sure of a realist use case.
