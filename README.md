# Python Indexed Priority Queue

A Python implementation of an Indexed Priority Queue (IPQ). This data structure has the following time complexities:

| Operation                                           | Description                                                 | Time Complexity |
| --------------------------------------------------- | ----------------------------------------------------------- | --------------- |
| push(key: Hashable, priority: Number) -> None       | Enqueue a key with a priority                               | O(log(n))       |
| pop() -> key: Hashable, priority: Number            | Retrieve the index with the highest priority (lowest value) | O(log(n))       |
| delete(key) -> key: Hashable, priority: Number      | Delete a key                                                | O(log(n))       |
| update(key: Hashable, new_priority: Number) -> None | Update the priority of a key                                | O(log(n))       |
| index(key: Hashable) -> int                         | Retrieve the index of a key                                 | O(1)            |
| key(index: int) -> Hashable                         | Membership check of a key                                   | O(1)            |
| priority(key: Hashable) -> Number                   | Retrieve the priority of a key                              | O(1)            |
| \_\_bool\_\_ -> bool                                | Determine if it's empty or not. Equivalent to is_empty()    | O(1)            |
| \_\_len\_\_ -> int                                  | Returns the number of elements in the queue                 | O(1)            |
| \_\_contains(key: Hashable)\_\_ -> bool             | Determine if a key is in the queue                          | O(1)            |
