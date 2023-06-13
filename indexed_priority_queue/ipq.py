from numbers import Number
from typing import Dict, Hashable, List, Tuple


class IndexedPriorityQueue:
    def __init__(self):
        self.queue: List[Number] = []
        self.key_index: Dict[Hashable, int] = {}  # key -> index in heap
        self.index_key: Dict[int, Hashable] = {}  # index in heap -> key

    def __bool__(self) -> bool:
        return bool(self.queue)

    def __len__(self) -> int:
        return len(self.queue)

    def __contains__(self, key: Hashable) -> bool:
        return key in self.key_index

    def index(self, key: Hashable) -> int:
        return self.key_index[key]

    def key(self, index: int) -> Hashable:
        return self.index_key[index]

    def priority(self, key: Hashable) -> Number:
        index = self.index(key)
        return self.queue[index]

    def peek(self) -> Tuple[Hashable, Number]:
        if len(self.queue) == 0:
            raise IndexError()

        return self.key(0), self.queue[0]

    def push(self, key: Hashable, priority: Number) -> None:
        if key in self.key_index:
            raise KeyError("Key already exists")

        self.queue.append(priority)

        index = len(self.queue) - 1

        self.key_index[key] = index
        self.index_key[index] = key

        self._maintain_invariant(index)

    def pop(self) -> Tuple[Hashable, Number]:
        if len(self.queue) == 0:
            raise IndexError()

        if len(self.queue) == 1:
            index = 0
            key = self.index_key[index]

            priority = self.queue.pop()

            del self.index_key[index]
            del self.key_index[key]

            return key, priority

        if len(self.queue) > 1:
            index = 0
            key = self.index_key[index]
            priority = self.queue[index]

            last_index = len(self.queue) - 1
            last_key = self.index_key[last_index]
            last_priority = self.queue.pop()

            self.queue[index] = last_priority

            del self.key_index[key]
            del self.index_key[last_index]

            self.index_key[index] = last_key
            self.key_index[last_key] = index

            self._maintain_invariant(0)

            return key, priority

    def delete(self, key: Hashable) -> Tuple[Hashable, Number]:
        index = self.index(key)

        if len(self.queue) == 1:
            return self.pop()

        priority = self.queue[index]

        last_index = len(self.queue) - 1
        last_key = self.index_key[last_index]
        last_priority = self.queue.pop()

        del self.key_index[key]
        del self.index_key[last_index]

        if index != last_index:
            self.queue[index] = last_priority

            self.key_index[last_key] = index
            self.index_key[index] = last_key

            self._maintain_invariant(index)

        return key, priority

    def update(self, key: Hashable, new_priority: Number) -> None:
        index = self.index(key)

        self.queue[index] = new_priority

        self._maintain_invariant(index)

    def _maintain_invariant(self, index: int) -> None:
        self._move_down(index)
        self._move_up(index)

    def _move_up(self, index) -> None:
        parent_index = (index - 1) // 2

        if index > 0 and self.queue[parent_index] > self.queue[index]:
            self._swap(index, parent_index)
            self._move_up(parent_index)

    def _swap(self, index_a: int, index_b: int) -> None:
        key_a = self.index_key[index_a]
        key_b = self.index_key[index_b]

        # Swap priorities in heap
        self.queue[index_a], self.queue[index_b] = (
            self.queue[index_b],
            self.queue[index_a],
        )

        # Swap mappings
        self.key_index[key_a], self.key_index[key_b] = index_b, index_a
        self.index_key[index_a], self.index_key[index_b] = key_b, key_a

    def _move_down(self, index: int) -> None:
        left_child_index = index * 2 + 1

        if (
            left_child_index < len(self.queue)
            and self.queue[left_child_index] < self.queue[index]
        ):
            self._swap(index, left_child_index)
            self._move_down(left_child_index)

        right_child_index = index * 2 + 2

        if (
            right_child_index < len(self.queue)
            and self.queue[right_child_index] < self.queue[index]
        ):
            self._swap(index, right_child_index)
            self._move_down(right_child_index)
