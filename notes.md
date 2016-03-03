### Notes for fluent-python

#### Chapter V

1. Any other regularity in the code is a sign, to me at least, that I'm using abstractions that aren't powerful enough.

-- Paul Graham

2. Ietrator pattern could scan one at a time and on demand, not in memory totally.

3. How the *iter()* function work:
>  Whenever the interpreter needs to interate an object **x**, it automatically calls **iter()**.
>  1. Checks whether the object implemts, \__iter\__, and calls that to obtain an iterator.
>  2. If __iter__ is not implements, but __getitem__ has, python creates an iterator that attempts to fetch items in order, starting from index 0.
>  3. If that fails, will raise TypeError

4. The standard interface for an iterator has two methods:

> __next__ : returns the next available item, raising StopIteration when there are no more items.
> __iter__ : returns self; this allows iterators to be used where an iterable is excepted, for example, in a loop.