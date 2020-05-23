import queue
import unittest
from dataclasses import dataclass
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int  # should put on the first
    data: Any

    def __init__(self, priority, data):
        self.priority = priority
        self.data = data


class PriorityQueueTest(unittest.TestCase):

    def test_put_get(self):
        q = queue.PriorityQueue()
        q.put((3, 'data 1'))
        q.put((4, 'data 2'))
        q.put((1, 'data 3'))
        q.put((2, 'data 4'))

        self.assertEqual((1, 'data 3'), q.get())
        self.assertEqual((2, 'data 4'), q.get())
        self.assertEqual((3, 'data 1'), q.get())
        self.assertEqual((4, 'data 2'), q.get())

    def test_put_get_prioritized_item(self):
        q = queue.PriorityQueue()
        q.put(PrioritizedItem(3, 'data 1'))
        q.put(PrioritizedItem(4, 'data 2'))
        q.put(PrioritizedItem(1, 'data 3'))
        q.put(PrioritizedItem(2, 'data 4'))

        self.assertEqual(PrioritizedItem(1, 'data 3'), q.get())
        self.assertEqual(PrioritizedItem(2, 'data 4'), q.get())
        self.assertEqual(PrioritizedItem(3, 'data 1'), q.get())
        self.assertEqual(PrioritizedItem(4, 'data 2'), q.get())


if __name__ == '__main__':
    unittest.main()
