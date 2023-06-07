from unittest import TestCase
from unittest.mock import Mock, MagicMock
from heapq import heappush, heappop
from indexed_priority_queue import IndexedPriorityQueue


LEFTMOST_INDEX = 0

PRIORITY_MOCK = Mock()
KEY_MOCK = Mock()


EXAMPLE_ELEMENTS = (
    (3, "Dan"),
    (1, "Lara"),
    (4, "Jack"),
    (6, "Kim"),
    (2, "Tom"),
    (5, "Max"),
)


class IndexedPriorityQueueTestCase(TestCase):
    def setUp(self):
        self.queue = IndexedPriorityQueue()

    def test_bool_when_empty(self):
        self.assertFalse(bool(self.queue))

    def test_bool_when_not_empty(self):
        self.queue.push(PRIORITY_MOCK, KEY_MOCK)
        self.assertTrue(bool(self.queue))

    def test_len_when_empty(self):
        self.assertEquals(len(self.queue), 0)

    def test_len_when_not_empty(self):
        self.queue.push(PRIORITY_MOCK, KEY_MOCK)
        self.assertEquals(len(self.queue), 1)

    def test_push_when_empty(self):
        self.queue.push(PRIORITY_MOCK, KEY_MOCK)

        self.assertEquals(self.queue.queue, [PRIORITY_MOCK])

        self.assertIn(KEY_MOCK, self.queue.key_index)
        self.assertEquals(self.queue.key_index[KEY_MOCK], LEFTMOST_INDEX)

        self.assertIn(LEFTMOST_INDEX, self.queue.index_key)
        self.assertEquals(self.queue.index_key[LEFTMOST_INDEX], KEY_MOCK)

    def test_push_with_examples(self):
        self.populate_with_examples()
        self.assert_invariant()

    def populate_with_examples(self):
        for priority, key in EXAMPLE_ELEMENTS:
            self.queue.push(priority, key)

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


q = IndexedPriorityQueue()

"""
q.push(3, "Dan")
q.push(1, "ALF")
q.push(4, "Jack")
q.push(2, "Tom")
q.push(5, "Max")


print(q.queue)
print("q.key_index", q.key_index)
print("q.index_key", q.index_key)


pop = q.pop()
print("pop", pop)
print("after pop", q.queue)
print("q.key_index", q.key_index)
print("q.index_key", q.index_key)

print("Jack exists", q.exists("Jack"))
print("Jack index", q.index("Jack"))

q.update("Jack", 0)
print("after update", q.queue)
print("q.key_index", q.key_index)
print("q.index_key", q.index_key)
print("Jack index", q.index("Jack"))
"""


"""
q = IndexedPriorityQueue()

people = [
    (4, "bob"), 
    (1, "john"), 
    (6, "tom"), 
    (7, "richard"), 
    (5, "jesus")
]

test = people[::]

for person in people:
    q.push(person)

print("before pop", q.queue)
# print("key_index", q.key_index)

pop = q.pop()
print("pop: ", pop)

print("after pop", q.queue)
#print("key_index", q.key_index)


#print("is tom in queue", q.exists((6, "tom")))
#print("index of tom in queue", q.index((6, "tom")))

q.delete((5, "jesus"))

print("after delete", q.queue)
"""

"""
print("----------------")

heapify(test)
print("test", test)

pop = heappop(test)
print("pop: ", pop)

print("after pop", test)
"""

from random import randrange


def test():
    values = set(  # To avoid repeated values
        [randrange(999) for i in range(randrange(9999))]
    )

    print("values: ", len(values), values)

    print("has repeated elements: ", len(values) != len(set(values)))

    heap = []
    queue = IndexedPriorityQueue()

    fill(heap, queue, values)

    pop_all(heap, queue)


def fill(heap, queue, values):
    for value in values:
        heappush(heap, value)
        queue.push(value)
        assert queue.queue == heap


def pop_all(heap, queue):
    while queue or heap:
        heap_value = heappop(heap)
        queue_value = queue.pop()
        assert heap_value == queue_value


# test()

"""
heap = []
heappush(heap, 8)
print(heap)
heappush(heap, 8)
print(heap)
"""
