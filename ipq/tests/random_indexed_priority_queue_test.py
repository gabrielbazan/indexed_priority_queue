from collections import defaultdict
from operator import add, sub
from random import choice, randrange

from ipq.indexed_priority_queue import IndexedPriorityQueue
from ipq.tests.base_indexed_priority_queue_test_case import (
    BaseIndexedPriorityQueueTestCase,
)


class RandomIndexedPriorityQueueTestCase(BaseIndexedPriorityQueueTestCase):
    RUNS = 50

    @property
    def operations(self):
        return [self.push, self.pop, self.delete, self.update]

    def setUp(self):
        self.queue = IndexedPriorityQueue()

    def test(self):
        # Runs the random tests multiple times
        for i in range(RandomIndexedPriorityQueueTestCase.RUNS):
            self.setUp()
            self.do_test()

    def do_test(self):
        """
        Pushes three quarters of the generated random values. Then runs
        random operations until all remaining values have been pushed.
        """
        elements = RandomIndexedPriorityQueueTestCase.generate_random_elements()

        half = len(elements) // 2

        left_half = elements[:half]
        right_half = elements[half:]

        self.push_elements(left_half)
        self.assert_invariant()

        while right_half and self.queue:
            operation = choice(self.operations)

            if operation == self.push:
                self.push(right_half)
            else:
                operation()

            self.assert_invariant()

    def push(self, remnant_values):
        key, priority = remnant_values.pop()
        self.queue.push(key, priority)

    def pop(self):
        self.queue.pop()

    def delete(self):
        key = choice(list(self.queue.key_index.keys()))
        self.queue.delete(key)

    def update(self):
        key = choice(list(self.queue.key_index.keys()))
        priority = self.queue.priority(key)
        op = choice([add, sub])
        self.queue.update(key, op(priority, randrange(20)))

    def push_elements(self, elements):
        for key, priority in elements:
            self.queue.push(key, priority)

    @staticmethod
    def generate_random_elements():
        # Keys must be unique; different keys may have the same priority
        elements = {}

        priorities = [randrange(70) for i in range(randrange(200))]

        counts = defaultdict(lambda: 0)

        for priority in priorities:
            key = f"key_{priority}_{counts[priority]}"
            elements[key] = priority
            counts[priority] += 1

        return list(elements.items())
