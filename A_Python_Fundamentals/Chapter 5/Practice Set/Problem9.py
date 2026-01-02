#Can you change the value inside a list which is contained in a set s ?
s = {8,7,12,[1,2]}
"""No, you cannot change the value inside a list that is contained in a set because lists are mutable, and sets require all their elements to be immutable (i.e., hashable). If you try to include a list in a set, Python will raise a `TypeError`.

For example, the following code:

```python
s = {8, 7, 12, [1, 2]}
```

will result in this error:
```
TypeError: unhashable type: 'list'
```

If you need to use mutable objects like lists but still want set-like behavior, you can either:

- Use a tuple instead of a list, as tuples are immutable:

  ```python
  s = {8, 7, 12, (1, 2)}  # Tuples are allowed in sets
  ```

- Use a `frozenset`, which is an immutable version of a set:

  ```python
  s = {8, 7, 12, frozenset([1, 2])}
  ```"""