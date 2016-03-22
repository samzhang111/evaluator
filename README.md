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

demo_evaluator = Evaluator()
result_of_block = demo_evaluator.evaluate(src) # This will be 1, and save "a" and "b" in demo_evaluator's namespace
```

Multiline statements that do not end with an expression will be executed and return None.

I am checking whether the final statement is an expression statement (ast.Expr). I don't know if there is a better way
of doing this. Drop me a line if you know better. :)

