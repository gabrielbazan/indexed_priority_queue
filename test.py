from heapq import heappush, heappop, heapify


class Element:
    
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value


class IndexedPriorityQueue:

    def __init__(self):
        self.queue = []

        self.key_indices = {}

        self.key_pos = {}  # key -> position

    def __bool__(self):
        return bool(self.queue)

    def push(self, item):
        self.queue.append(item)

        position = len(self.queue) - 1

        self.key_pos[item] = position

        self._bubble_up(position)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.queue[parent_index] > self.queue[index]:
            self._swap(index, parent_index)
            self._bubble_up(parent_index)

    def _swap(self, index_a, index_b):
        item_a = self.queue[index_a]
        item_b = self.queue[index_b]

        self.queue[index_a], self.queue[index_b] = self.queue[index_b], self.queue[index_a]

        self.key_pos[item_a], self.key_pos[item_b] =  index_b, index_a

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError()

        if len(self.queue) == 1:
            item = self.queue.pop()
            del self.key_pos[item]
            return item

        if len(self.queue) > 1:
            item = self.queue[0]

            last_item = self.queue.pop()
            self.queue[0] = last_item

            del self.key_pos[item]

            self._bubble_down(0)

            return item

    def _bubble_down(self, index):
        left_child_index = index * 2 + 1

        if left_child_index < len(self.queue) and self.queue[left_child_index] < self.queue[index]:
            self._swap(index, left_child_index)
            self._bubble_down(left_child_index)

        right_child_index = index * 2 + 2
        if right_child_index < len(self.queue) and self.queue[right_child_index] < self.queue[index]:
            self._swap(index, right_child_index)
            self._bubble_down(right_child_index)

    def exists(self, item):
        return item in self.key_pos

    def index(self, item):
        return self.key_pos.get(item) 

    def delete(self, item):
        if not self.exists(item):
            raise IndexError()
        
        index = self.index(item)

        last_item = self.queue.pop()

        self.queue[index] = last_item

        self._bubble_down(index)
        self._bubble_up(index)

    def update(self, item, new_item):
        if not self.exists(item):
            raise IndexError()

        index = self.index(item)

        self.queue[index] = new_item

        self._bubble_down(index)
        self._bubble_up(index)


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
# print("key_pos", q.key_pos)

pop = q.pop()
print("pop: ", pop)

print("after pop", q.queue)
#print("key_pos", q.key_pos)


#print("is tom in queue", q.exists((6, "tom")))
#print("index of tom in queue", q.index((6, "tom")))

q.delete((5, "jesus"))

print("after delete", q.queue)


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
    values = [
        randrange(999)
        for i in range(randrange(9999))
    ]

    print("values: ", len(values), values)

    print("has repeated elements: ", len(values) != set(values))

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

heap = []
heappush(heap, 8)
print(heap)
heappush(heap, 8)
print(heap)