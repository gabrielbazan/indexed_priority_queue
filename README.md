# Python Indexed Priority Queue

A Python implementation of an Indexed Priority Queue (IPQ).

An IPQ is like any regular priority queue. But it supports quick lookups, updates and deletions...on the fly.

<p align="center">
    <a href="https://github.com/gabrielbazan/indexed_priority_queue/actions"><img alt="Test Workflow Status" src="https://github.com/gabrielbazan/indexed_priority_queue/workflows/Test/badge.svg"></a>
    <a href="https://github.com/gabrielbazan/indexed_priority_queue/actions"><img alt="Linting Workflow Status" src="https://github.com/gabrielbazan/indexed_priority_queue/workflows/Lint/badge.svg"></a>
    <a href="https://github.com/gabrielbazan/indexed_priority_queue/actions"><img alt="PyPI Publication Workflow Status" src="https://github.com/gabrielbazan/indexed_priority_queue/workflows/Publish%20to%20PyPI/badge.svg"></a>
    <a href="https://coveralls.io/github/gabrielbazan/indexed_priority_queue?branch=main"><img alt="Coverage Status" src="https://coveralls.io/repos/github/gabrielbazan/indexed_priority_queue/badge.svg?branch=main"></a>
    <a href="https://pypi.org/project/indexed_priority_queue/"><img alt="PyPI" src="https://img.shields.io/pypi/v/indexed_priority_queue"></a>
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Time and space complexities

It is implemented as minimum binary heap. For indexing, it uses two additional dicts. So, in terms of memory space, it uses _O(3 \* n) -> O(n)_ space.

This data structure has the following time complexities:

| Operation                      | Description                                                                 | Time Complexity |
| ------------------------------ | --------------------------------------------------------------------------- | --------------- |
| `push(key, priority)`          | Enqueue a key with a priority                                               | O(log(n))       |
| `pop() -> key, priority`       | Pop and retrieve the index with the highest priority (lowest value)         | O(log(n))       |
| `peek() -> key, priority`      | Retrieve the key and priority with the highest priority, without popping it | O(1)            |
| `delete(key) -> key, priority` | Delete a key                                                                | O(log(n))       |
| `update(key, new_priority)`    | Update the priority of a key                                                | O(log(n))       |
| `index(key) -> int`            | Retrieve the index of the given key                                         | O(1)            |
| `key(index: int)`              | Retrieve the key at the given index                                         | O(1)            |
| `priority(key)`                | Retrieve the priority of the given key                                      | O(1)            |
| `__bool__ -> bool`             | Determine if the queue is empty or not. Equivalent to _is_empty()_          | O(1)            |
| `__len__ -> int`               | Returns the count of elements in the queue                                  | O(1)            |
| `__contains(key)__ -> bool`    | Determine if the given key exists in the queue                              | O(1)            |

Where:

1. `key` is any `typing.Hashable` object
2. `priority` is a `numbers.Number`
3. `index` is an `int`

## Examples

```python
from indexed_priority_queue import IndexedPriorityQueue


# Initialize the queue
queue = IndexedPriorityQueue()

# Enqueue a few values
queue.push("John", 7)
queue.push("Maria", 3)
queue.push("Peter", 5)

key, priority = queue.peek()  # Maria, 3

queue.push("Kim", 2)
key, priority = queue.peek()  # Kim, 2

queue.update("Peter", 1)
key, priority = queue.peek()  # Peter, 1

assert len(queue) == 4  # True
key, priority = queue.delete("John")  # John, 7
assert len(queue) == 3  # True

key, priority = queue.pop()  # Peter, 1

key, priority = queue.peek()  # Kim, 2
index = queue.index("Kim")  # 0
key = queue.key(0)  # Kim
priority = queue.priority("Kim")  # 2

# Not empty, 2
if queue:
    print(f"Not empty, {len(queue)}")
else:
    print("Empty")

# Max is not in the queue
if "Max" in queue:
    print("Max is in the queue")
else:
    print("Max is not in the queue")
```

- `push` raises `KeyError` if the key is already in the queue.
- `pop` and `peek` raise `IndexError` if the queue is empty.
- `delete`, `update`, `index` and `priority` raise `KeyError` if the key is not in the queue.
- `key` raises `KeyError` if the given index does not exist.


## Use any hashable object as key

You can use any `typing.Hashable` object as key, not just strings. For example:

```python
queue.push(frozenset(["a", "b"]), 1)
queue.push((1, 2, 3), 2)
```
