# Python Indexed Priority Queue

A Python implementation of an Indexed Priority Queue (IPQ). This data structure has the following time complexities:

| Operation                         | Description                                                 | Time Complexity |
| --------------------------------- | ----------------------------------------------------------- | --------------- |
| push(key, priority) -> None       | Add a key with a priority                                   | O(log(n))       |
| pop() -> priority, key            | Retrieve the index with the highest priority (lowest value) | O(log(n))       |
| delete(key) -> priority, key      | Delete a key                                                | O(log(n))       |
| update(key, new_priority) -> None | Update the priority of a key                                | O(log(n))       |
| index(key) -> int                 | Retrieve the index of a key                                 | O(1)            |
| key(index)                        | Membership check                                            | O(1)            |
| priority(key)                     | Retrieve the priority of a key                              | O(1)            |
| \_\_bool\_\_ -> bool              | Determine if it's empty or not. Equivalent to is_empty()    | O(1)            |
| \_\_len\_\_ -> int                | Returns the number of elements in the queue                 | O(1)            |
| \_\_contains(key)\_\_ -> bool     | Determine if a key is in the queue                          | O(1)            |
