from unittest import TestCase

from ipq.indexed_priority_queue import IndexedPriorityQueue


class BaseIndexedPriorityQueueTestCase(TestCase):
    def setUp(self):
        self.queue = IndexedPriorityQueue()

    def assert_invariant(self):
        heap_size = len(self.queue)

        for root in range(heap_size):
            left = 2 * root + 1
            right = 2 * root + 2

            self.assert_child_invariant(heap_size, root, left)
            self.assert_child_invariant(heap_size, root, right)

    def assert_child_invariant(self, heap_size, root_index, child_index):
        if child_index < heap_size:
            self.assertLessEqual(root_index, child_index)
