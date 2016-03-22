#Evaluator

A proof-of-concept for evaluating multiline Python blocks.

Example:

```python
from evaluator import Evaluator
src = """
a = 1
b = 2
a
"""

e = Evaluator(src)
result_of_block = e.evaluate() # This will be 1
```

Multiline statements that do not end with an expression will be executed and return None.

I am using a heuristic for determining whether an expression is evaluable from an evening of poking around
with Python ASTs, and that is whether a statement has only `lineno`, `col_offset`, and `value` as its public
attributes. There might be obvious limitations to doing this, or better ways. Drop me a line if you
know better. :)

