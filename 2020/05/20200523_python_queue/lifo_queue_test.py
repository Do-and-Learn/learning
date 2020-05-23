import queue
import unittest


class LifoQueueTest(unittest.TestCase):

    def test_put_get(self):
        q = queue.LifoQueue()
        q.put('data 1')
        q.put('data 2')
        q.put('data 3')

        self.assertEqual('data 3', q.get())
        self.assertEqual('data 2', q.get())
        self.assertEqual('data 1', q.get())


if __name__ == '__main__':
    unittest.main()
