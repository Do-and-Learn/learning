import queue
import unittest


class SimpleQueueTest(unittest.TestCase):

    def test_qsize(self):
        q = queue.SimpleQueue()
        self.assertEqual(0, q.qsize())
        q.put('data 1')
        self.assertEqual(1, q.qsize())
        q.put('data 2')
        self.assertEqual(2, q.qsize())

        self.assertEqual('data 1', q.get())
        self.assertEqual(1, q.qsize())

        self.assertEqual('data 2', q.get())
        self.assertEqual(0, q.qsize())

    def test_empty(self):
        q = queue.SimpleQueue()
        self.assertTrue(q.empty())
        q.put('data 1')
        self.assertFalse(q.empty())
        q.get()
        self.assertTrue(q.empty())

    def test_put_get(self):
        q = queue.SimpleQueue()
        q.put('data 1')
        q.put('data 2')

        self.assertEqual('data 1', q.get())
        self.assertEqual('data 2', q.get())

    def test_put_get_nowait(self):
        q = queue.SimpleQueue()
        q.put_nowait('data 1')
        q.put_nowait('data 2')

        self.assertEqual('data 1', q.get_nowait())
        self.assertEqual('data 2', q.get_nowait())


if __name__ == '__main__':
    unittest.main()
