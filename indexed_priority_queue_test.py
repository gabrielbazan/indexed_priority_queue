from unittest import TestCase
from unittest.mock import Mock
from random import randrange, choice
from operator import add, sub
from indexed_priority_queue import IndexedPriorityQueue


LEFTMOST_INDEX = 0

PRIORITY_MOCK = Mock()
KEY_MOCK = Mock()


EXAMPLE_TOP_PRIORITY = 1
EXAMPLE_TOP_PRIORITY_KEY = "Lara"

EXAMPLE_ELEMENTS = (
    (3, "Dan"),
    (4, "Jack"),
    (9, "Marge"),
    (6, "Kim"),
    (12, "Jim"),
    (11, "Homer"),
    (EXAMPLE_TOP_PRIORITY, EXAMPLE_TOP_PRIORITY_KEY),
    (2, "Tom"),
    (10, "Nelson"),
    (5, "Max"),
    (7, "Anna"),
    (8, "Leo"),
)


class IndexedPriorityQueueBaseTestCase(TestCase):
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


class IndexedPriorityQueueTestCase(IndexedPriorityQueueBaseTestCase):
    def test_bool_when_empty(self):
        self.assertFalse(bool(self.queue))

    def test_bool_when_not_empty(self):
        self.push_mocked_element_to_queue()
        self.assertTrue(bool(self.queue))

    def push_mocked_element_to_queue(self):
        self.queue.push(KEY_MOCK, PRIORITY_MOCK)

    def test_len_when_empty(self):
        self.assertEquals(len(self.queue), 0)

    def test_len_when_not_empty(self):
        self.push_mocked_element_to_queue()
        self.assertEquals(len(self.queue), 1)

    def test_contains_when_not_contained(self):
        self.assertFalse(KEY_MOCK in self.queue)

    def test_contains_when_contained(self):
        self.push_mocked_element_to_queue()
        self.assertTrue(KEY_MOCK in self.queue)

    def test_index_when_index_does_not_exists(self):
        with self.assertRaises(KeyError):
            self.queue.index(KEY_MOCK)

    def test_index_when_index_exists(self):
        self.push_mocked_element_to_queue()
        self.assertEquals(self.queue.index(KEY_MOCK), LEFTMOST_INDEX)

    def test_push_when_empty(self):
        self.push_mocked_element_to_queue()

        self.assertEquals(self.queue.queue, [PRIORITY_MOCK])

        self.assertIn(KEY_MOCK, self.queue.key_index)
        self.assertEquals(self.queue.key_index[KEY_MOCK], LEFTMOST_INDEX)

        self.assertIn(LEFTMOST_INDEX, self.queue.index_key)
        self.assertEquals(self.queue.index_key[LEFTMOST_INDEX], KEY_MOCK)

    def test_push_with_examples(self):
        self.push_example_values()
        self.assert_invariant()

    def push_example_values(self):
        for priority, key in EXAMPLE_ELEMENTS:
            self.queue.push(key, priority)

    def test_pop_when_empty(self):
        with self.assertRaises(IndexError):
            self.queue.pop()
        self.assert_invariant()

    def test_pop_when_queue_has_only_one_element(self):
        self.push_mocked_element_to_queue()

        popped_priority, popped_key = self.queue.pop()

        self.assertIs(popped_priority, PRIORITY_MOCK)
        self.assertIs(popped_key, KEY_MOCK)

        self.assertEquals(len(self.queue), 0)
        self.assertEquals(len(self.queue.key_index), 0)
        self.assertEquals(len(self.queue.index_key), 0)

        self.assert_invariant()

    def test_pop_when_queue_has_multiple_elements(self):
        self.push_example_values()

        previous_length = len(self.queue)
        last_element_index = previous_length - 1

        popped_priority, popped_key = self.queue.pop()

        self.assertIs(popped_priority, EXAMPLE_TOP_PRIORITY)
        self.assertIs(popped_key, EXAMPLE_TOP_PRIORITY_KEY)

        self.assertEquals(len(self.queue), previous_length - 1)

        self.assertNotIn(popped_key, self.queue.key_index)
        self.assertNotIn(last_element_index, self.queue.index_key)

        self.assert_invariant()

    def test_delete_when_empty(self):
        with self.assertRaises(KeyError):
            self.queue.delete(KEY_MOCK)

    def test_delete_when_key_does_not_exist(self):
        self.push_mocked_element_to_queue()
        non_existent_key = Mock()

        with self.assertRaises(KeyError):
            self.queue.delete(non_existent_key)

    def test_delete_when_it_has_only_one_element(self):
        self.push_mocked_element_to_queue()

        priority, key = self.queue.delete(KEY_MOCK)

        self.assertIs(priority, PRIORITY_MOCK)
        self.assertIs(key, KEY_MOCK)

        self.assertEquals(len(self.queue), 0)
        self.assertEquals(len(self.queue.key_index), 0)
        self.assertEquals(len(self.queue.index_key), 0)

    def test_delete_from_the_middle(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        middle_index = length // 2
        middle_priority = self.queue.queue[middle_index]
        middle_key = self.queue.key(middle_index)

        deleted_priority, deleted_key = self.queue.delete(middle_key)

        self.assertIs(deleted_priority, middle_priority)
        self.assertIs(deleted_key, middle_key)

        self.assertEquals(len(self.queue), length - 1)

        self.assertNotIn(middle_key, self.queue.key_index)
        self.assertNotIn(last_index, self.queue.index_key)

        self.assert_invariant()

    def test_delete_last_element(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        last_priority = self.queue.queue[last_index]
        last_key = self.queue.key(last_index)

        deleted_priority, deleted_key = self.queue.delete(last_key)

        self.assertIs(deleted_priority, last_priority)
        self.assertIs(deleted_key, last_key)

        self.assertEquals(len(self.queue), length - 1)

        self.assertNotIn(last_key, self.queue.key_index)
        self.assertNotIn(last_index, self.queue.index_key)

        self.assert_invariant()

    def test_update_when_key_does_not_exist(self):
        self.push_mocked_element_to_queue()

        non_existent_key = Mock()
        priority_mock = Mock()

        with self.assertRaises(KeyError):
            self.queue.update(non_existent_key, priority_mock)

    def test_update_when_lowering_priority_of_root(self):
        self.push_example_values()

        previous_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertEquals(previous_index, 0)

        self.queue.update(EXAMPLE_TOP_PRIORITY_KEY, EXAMPLE_TOP_PRIORITY + 3)

        # Not the first anymore
        new_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertNotEquals(new_index, 0)

        self.assert_invariant()

    def test_update_when_increasing_priority_of_root(self):
        self.push_example_values()

        previous_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertEquals(previous_index, 0)

        self.queue.update(EXAMPLE_TOP_PRIORITY_KEY, EXAMPLE_TOP_PRIORITY - 2)

        # Still the first
        new_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertEquals(new_index, 0)

        self.assert_invariant()

    def test_update_when_increasing_priority_of_last_leaf(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        last_key = self.queue.key(last_index)
        last_priority = self.queue.priority(last_key)

        self.queue.update(last_key, last_priority - 4)

        # Not the last anymore
        new_index = self.queue.index(last_key)
        self.assertNotEquals(new_index, last_index)

        self.assert_invariant()

    def test_update_when_lowering_priority_of_last_leaf(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        last_key = self.queue.key(last_index)
        last_priority = self.queue.priority(last_key)

        self.queue.update(last_key, last_priority + 3)

        # Still the last
        new_index = self.queue.index(last_key)
        self.assertEquals(new_index, last_index)

        self.assert_invariant()

    def test_update_when_increasing_priority_of_last_leaf_to_be_the_root(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        last_key = self.queue.key(last_index)

        self.queue.update(last_key, EXAMPLE_TOP_PRIORITY - 1)

        # The last leaf is now the root
        new_index = self.queue.index(last_key)
        self.assertEquals(new_index, 0)

        self.assert_invariant()

    def test_update_when_lowering_priority_at_the_middle(self):
        self.push_example_values()

        middle_index = 1  # What's important is that it's not a leaf, nor the root
        middle_key = self.queue.key(middle_index)
        middle_priority = self.queue.priority(middle_key)

        self.queue.update(middle_key, middle_priority + 10)

        # It has been pushed downwards
        new_index = self.queue.index(middle_key)
        self.assertGreater(new_index, middle_index)

        self.assert_invariant()

    def test_update_when_increasing_priority_at_the_middle(self):
        self.push_example_values()

        middle_index = 1  # What's important is that it's not a leaf, nor the root
        middle_key = self.queue.key(middle_index)
        middle_priority = self.queue.priority(middle_key)

        self.queue.update(middle_key, middle_priority - 10)

        # It has been pushed upwards
        new_index = self.queue.index(middle_key)
        self.assertLess(new_index, middle_index)

        self.assert_invariant()


class IndexedPriorityQueueRandomTestCase(IndexedPriorityQueueBaseTestCase):
    RUNS = 50

    @property
    def operations(self):
        return [self.push, self.pop, self.delete, self.update]

    def setUp(self):
        self.queue = IndexedPriorityQueue()

    def test(self):
        # Runs the random tests multiple times
        for i in range(IndexedPriorityQueueRandomTestCase.RUNS):
            self.do_test()

    def do_test(self):
        """
        Pushes three quarters of the generated random values. Then runs
        random operations until all remaining values have been pushed.
        """
        values = IndexedPriorityQueueRandomTestCase.generate_random_values()

        three_quarters = values[: len(values) // 4 * 3]
        remnant_values = values[len(values) // 4 * 3 :]

        self.push_values(three_quarters)
        self.assert_invariant()

        while remnant_values:
            operation = choice(self.operations)

            if operation == self.push:
                self.push(remnant_values)
            else:
                operation()

            self.assert_invariant()

    def push(self, remnant_values):
        value = remnant_values.pop()
        self.queue.push(f"key_{value}", value)

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

    def push_values(self, values):
        for value in values:
            self.queue.push(f"key_{value}", value)

    @staticmethod
    def generate_random_values():
        # As for now, we do not support repeated values
        return list(set([randrange(9999) for i in range(randrange(100))]))
