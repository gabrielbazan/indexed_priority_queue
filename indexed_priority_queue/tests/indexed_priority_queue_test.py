from unittest.mock import Mock

from indexed_priority_queue.tests.base_indexed_priority_queue_test_case import (
    BaseIndexedPriorityQueueTestCase,
)

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
    (2, "Peter"),
    (12, "Jim"),
    (11, "Homer"),
    (EXAMPLE_TOP_PRIORITY, EXAMPLE_TOP_PRIORITY_KEY),
    (2, "Tom"),
    (10, "Nelson"),
    (3, "Justin"),
    (5, "Max"),
    (7, "Anna"),
    (8, "Leo"),
)


class IndexedPriorityQueueTestCase(BaseIndexedPriorityQueueTestCase):
    def test_bool_when_empty(self):
        self.assertFalse(bool(self.queue))

    def test_bool_when_not_empty(self):
        self.push_mocked_element_to_queue()
        self.assertTrue(bool(self.queue))

    def push_mocked_element_to_queue(self):
        self.queue.push(KEY_MOCK, PRIORITY_MOCK)

    def test_len_when_empty(self):
        self.assertEqual(len(self.queue), 0)

    def test_len_when_not_empty(self):
        self.push_mocked_element_to_queue()
        self.assertEqual(len(self.queue), 1)

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
        self.assertEqual(self.queue.index(KEY_MOCK), LEFTMOST_INDEX)

    def test_priority_when_key_does_not_exist(self):
        with self.assertRaises(KeyError):
            self.queue.priority(KEY_MOCK)

    def test_priority_when_key_exists(self):
        self.push_mocked_element_to_queue()

        returned_priority = self.queue.priority(KEY_MOCK)

        self.assertIs(returned_priority, PRIORITY_MOCK)

    def test_push_when_empty(self):
        self.push_mocked_element_to_queue()

        self.assertEqual(self.queue.queue, [PRIORITY_MOCK])

        self.assertIn(KEY_MOCK, self.queue.key_index)
        self.assertEqual(self.queue.key_index[KEY_MOCK], LEFTMOST_INDEX)

        self.assertIn(LEFTMOST_INDEX, self.queue.index_key)
        self.assertEqual(self.queue.index_key[LEFTMOST_INDEX], KEY_MOCK)

    def test_push_with_examples(self):
        self.push_example_values()

        self.assertEqual(len(self.queue), len(EXAMPLE_ELEMENTS))
        self.assertEqual(len(self.queue.index_key), len(EXAMPLE_ELEMENTS))
        self.assertEqual(len(self.queue.key_index), len(EXAMPLE_ELEMENTS))

        self.assert_invariant()

    def push_example_values(self):
        for priority, key in EXAMPLE_ELEMENTS:
            self.queue.push(key, priority)

    def test_push_with_duplicated_keys(self):
        self.push_mocked_element_to_queue()

        with self.assertRaises(KeyError):
            self.push_mocked_element_to_queue()

    def test_pop_when_empty(self):
        with self.assertRaises(IndexError):
            self.queue.pop()
        self.assert_invariant()

    def test_pop_when_queue_has_only_one_element(self):
        self.push_mocked_element_to_queue()

        popped_key, popped_priority = self.queue.pop()

        self.assertIs(popped_priority, PRIORITY_MOCK)
        self.assertIs(popped_key, KEY_MOCK)

        self.assertEqual(len(self.queue), 0)
        self.assertEqual(len(self.queue.key_index), 0)
        self.assertEqual(len(self.queue.index_key), 0)

        self.assert_invariant()

    def test_pop_when_queue_has_multiple_elements(self):
        self.push_example_values()

        previous_length = len(self.queue)
        last_element_index = previous_length - 1

        popped_key, popped_priority = self.queue.pop()

        self.assertIs(popped_priority, EXAMPLE_TOP_PRIORITY)
        self.assertIs(popped_key, EXAMPLE_TOP_PRIORITY_KEY)

        self.assertEqual(len(self.queue), previous_length - 1)

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

        key, priority = self.queue.delete(KEY_MOCK)

        self.assertIs(priority, PRIORITY_MOCK)
        self.assertIs(key, KEY_MOCK)

        self.assertEqual(len(self.queue), 0)
        self.assertEqual(len(self.queue.key_index), 0)
        self.assertEqual(len(self.queue.index_key), 0)

    def test_delete_from_the_middle(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        middle_index = length // 2
        middle_priority = self.queue.queue[middle_index]
        middle_key = self.queue.key(middle_index)

        deleted_key, deleted_priority = self.queue.delete(middle_key)

        self.assertIs(deleted_priority, middle_priority)
        self.assertIs(deleted_key, middle_key)

        self.assertEqual(len(self.queue), length - 1)

        self.assertNotIn(middle_key, self.queue.key_index)
        self.assertNotIn(last_index, self.queue.index_key)

        self.assert_invariant()

    def test_delete_last_element(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        last_priority = self.queue.queue[last_index]
        last_key = self.queue.key(last_index)

        deleted_key, deleted_priority = self.queue.delete(last_key)

        self.assertIs(deleted_priority, last_priority)
        self.assertIs(deleted_key, last_key)

        self.assertEqual(len(self.queue), length - 1)

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
        self.assertEqual(previous_index, 0)

        self.queue.update(EXAMPLE_TOP_PRIORITY_KEY, EXAMPLE_TOP_PRIORITY + 3)

        # Not the first anymore
        new_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertNotEqual(new_index, 0)

        self.assert_invariant()

    def test_update_when_increasing_priority_of_root(self):
        self.push_example_values()

        previous_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertEqual(previous_index, 0)

        self.queue.update(EXAMPLE_TOP_PRIORITY_KEY, EXAMPLE_TOP_PRIORITY - 2)

        # Still the first
        new_index = self.queue.index(EXAMPLE_TOP_PRIORITY_KEY)
        self.assertEqual(new_index, 0)

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
        self.assertNotEqual(new_index, last_index)

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
        self.assertEqual(new_index, last_index)

        self.assert_invariant()

    def test_update_when_increasing_priority_of_last_leaf_to_be_the_root(self):
        self.push_example_values()

        length = len(self.queue)
        last_index = length - 1
        last_key = self.queue.key(last_index)

        self.queue.update(last_key, EXAMPLE_TOP_PRIORITY - 1)

        # The last leaf is now the root
        new_index = self.queue.index(last_key)
        self.assertEqual(new_index, 0)

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

    def test_example(self):
        self.queue.push("John", 7)
        self.queue.push("Maria", 3)
        self.queue.push("Peter", 5)

        key, priority = self.queue.peek()
        self.assertEqual(key, "Maria")
        self.assertEqual(priority, 3)

        self.queue.push("Kim", 2)
        key, priority = self.queue.peek()
        self.assertEqual(key, "Kim")
        self.assertEqual(priority, 2)

        self.queue.update("Peter", 1)
        key, priority = self.queue.peek()
        self.assertEqual(key, "Peter")
        self.assertEqual(priority, 1)

        self.assertEqual(len(self.queue), 4)
        key, priority = self.queue.delete("John")
        self.assertEqual(key, "John")
        self.assertEqual(priority, 7)
        self.assertEqual(len(self.queue), 3)

        key, priority = self.queue.pop()
        self.assertEqual(key, "Peter")
        self.assertEqual(priority, 1)

        key, priority = self.queue.peek()
        self.assertEqual(key, "Kim")
        self.assertEqual(priority, 2)
        self.assertEqual(self.queue.index("Kim"), 0)
        self.assertEqual(self.queue.key(0), "Kim")
        self.assertEqual(self.queue.priority("Kim"), 2)

        self.assertTrue(bool(self.queue))

        self.assertFalse("Max" in self.queue)
        self.assertTrue("Maria" in self.queue)

    def test_with_hashable_objects(self):
        objects = (frozenset(["a", 1, 5.4]), (1, 2), "abc")

        for obj in objects:
            self.queue.push(obj, 1)

    def test_with_non_hashable_objects(self):
        objects = (["a", "b"], {"a": "b"}, {"a", "b"})

        for obj in objects:
            with self.assertRaises(TypeError):
                self.queue.push(obj, 1)
