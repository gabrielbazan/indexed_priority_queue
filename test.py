from heapq import heappush, heappop, heapify


# At first, do not support repeated values


class IndexedPriorityQueue:

    def __init__(self):
        self.queue = []
        self.key_index = {}  # key -> index in heap
        self.index_key = {}  # index in heap -> key

    def __bool__(self):
        return bool(self.queue)

    def push(self, priority, key):
        self.queue.append(priority)

        index = len(self.queue) - 1

        self.key_index[key] = index
        self.index_key[index] = key

        self._maintain_invariant(index)

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError()

        if len(self.queue) == 1:
            index = 0
            key = self.index_key[index]

            priority = self.queue.pop()

            del self.index_key[index]
            del self.key_index[key]

            return priority, key

        if len(self.queue) > 1:
            index = 0
            key = self.index_key[index]

            priority = self.queue[0]

            last_index = len(self.queue) - 1
            last_priority = self.queue.pop()

            self.queue[0] = last_priority

            del self.key_index[key]
            self.index_key[0] = self.index_key[last_index]
            del self.index_key[last_index]

            self._maintain_invariant(0)

            return priority, key

    def exists(self, key):
        return key in self.key_index

    def index(self, key):
        return self.key_index.get(key) 

    def delete(self, key):
        if not self.exists(key):
            raise IndexError()

        index = self.index(key)

        last_item = self.queue.pop()

        self.queue[index] = last_item

        # update mappings

        self._maintain_invariant(index)

    def update(self, key, new_priority):
        if not self.exists(key):
            raise IndexError()

        index = self.index(key)

        self.queue[index] = new_priority

        self._maintain_invariant(index)

    def _maintain_invariant(self, index):
        self._bubble_down(index)
        self._bubble_up(index)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.queue[parent_index] > self.queue[index]:
            self._swap(index, parent_index)
            self._bubble_up(parent_index)

    def _swap(self, index_a, index_b):
        key_a = self.index_key[index_a]
        key_b = self.index_key[index_b]

        # Swap priorities in heap
        self.queue[index_a], self.queue[index_b] = self.queue[index_b], self.queue[index_a]

        # Swap mappings
        self.key_index[key_a], self.key_index[key_b] =  index_b, index_a
        self.index_key[index_a], self.index_key[index_b] = key_b, key_a

    def _bubble_down(self, index):
        left_child_index = index * 2 + 1

        if left_child_index < len(self.queue) and self.queue[left_child_index] < self.queue[index]:
            self._swap(index, left_child_index)
            self._bubble_down(left_child_index)

        right_child_index = index * 2 + 2
        if right_child_index < len(self.queue) and self.queue[right_child_index] < self.queue[index]:
            self._swap(index, right_child_index)
            self._bubble_down(right_child_index)


q = IndexedPriorityQueue()


q.push(3, "Dan")
q.push(1, "ALF")
q.push(4, "Gabe")
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

print("Gabe exists", q.exists("Gabe"))
print("Gabe index", q.index("Gabe"))

q.update("Gabe", 0)
print("after update", q.queue)
print("q.key_index", q.key_index)
print("q.index_key", q.index_key)
print("Gabe index", q.index("Gabe"))


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
        [
            randrange(999)
            for i in range(randrange(9999))
        ]
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


#test()

"""
heap = []
heappush(heap, 8)
print(heap)
heappush(heap, 8)
print(heap)
"""