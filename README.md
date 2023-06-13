# Python Indexed Priority Queue

A Python implementation of an Indexed Priority Queue (IPQ).

It is implemented as minimum binary heap. For indexing, it uses two additional dicts. So, in terms of memory space, it uses _O(3 \* n) -> O(n)_.

This data structure has the following time complexities:

| Operation                      | Description                                                         | Time Complexity |
| ------------------------------ | ------------------------------------------------------------------- | --------------- |
| `push(key, priority)`          | Enqueue a key with a priority                                       | O(log(n))       |
| `pop() -> key, priority`       | Pop and retrieve the index with the highest priority (lowest value) | O(log(n))       |
| `delete(key) -> key, priority` | Delete a key                                                        | O(log(n))       |
| `update(key, new_priority)`    | Update the priority of a key                                        | O(log(n))       |
| `index(key) -> int`            | Retrieve the index of the given key                                 | O(1)            |
| `key(index: int)  `            | Retrieve the key at the given index                                 | O(1)            |
| `priority(key) -> Number `     | Retrieve the priority of the given key                              | O(1)            |
| `__bool__ -> bool`             | Determine if the queue is empty or not. Equivalent to _is_empty()_  | O(1)            |
| `__len__ -> int`               | Returns the count of elements in the queue                          | O(1)            |
| `__contains(key)__ -> bool`    | Determine if the given key exists in the queue                      | O(1)            |
