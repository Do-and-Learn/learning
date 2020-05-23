import _queue
import queue
import threading
import time
import unittest
from datetime import datetime


class QueueTest(unittest.TestCase):

    def test_qsize(self):
        q = queue.Queue()
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
        q = queue.Queue()
        self.assertTrue(q.empty())
        q.put('data 1')
        self.assertFalse(q.empty())
        q.get()
        self.assertTrue(q.empty())

    def test_full_infinity(self):
        q = queue.Queue()
        self.assertFalse(q.full())
        for i in range(100):
            q.put(i)
        self.assertFalse(q.full())

    def test_full_not_infinity(self):
        q = queue.Queue(1)
        self.assertFalse(q.full())
        q.put('data')
        self.assertTrue(q.full())

    def test_put_get(self):
        q = queue.SimpleQueue()
        q.put('data 1')
        q.put('data 2')
        q.put('data 3')

        self.assertEqual('data 1', q.get())
        self.assertEqual('data 2', q.get())
        self.assertEqual('data 3', q.get())

    def test_put_wait(self):
        q = queue.Queue(1)
        q.put('data 1')

        def deque():
            time.sleep(1)
            q.get()

        t = threading.Thread(target=deque)
        start_time = datetime.now()
        t.start()

        q.put('data 2')

        end_time = datetime.now()
        self.assertEqual(1, (end_time - start_time).seconds)

    def test_put_timeout(self):
        q = queue.Queue(1)
        q.put('data 1')
        with self.assertRaises(queue.Full) as context:
            start_time = datetime.now()
            q.put('data 2', timeout=1)
        end_time = datetime.now()
        self.assertEqual(1, (end_time - start_time).seconds)
        self.assertEqual(0, len(context.exception.args))

    def test_put_no_blocking(self):
        q = queue.Queue(1)
        q.put('data 1')
        with self.assertRaises(queue.Full) as context:
            start_time = datetime.now()
            q.put('data 2', block=False)
        end_time = datetime.now()
        self.assertEqual(0, (end_time - start_time).seconds)
        self.assertEqual(0, len(context.exception.args))

    def test_put_nowait(self):
        q = queue.Queue(1)
        q.put('data 1')
        with self.assertRaises(queue.Full) as context:
            start_time = datetime.now()
            q.put_nowait('data 2')
        end_time = datetime.now()
        self.assertEqual(0, (end_time - start_time).seconds)
        self.assertEqual(0, len(context.exception.args))

    def test_get(self):
        q = queue.Queue()

        def put_data():
            time.sleep(1)
            q.put('data')

        t = threading.Thread(target=put_data)
        start_time = datetime.now()
        t.start()

        data = q.get()
        end_time = datetime.now()
        self.assertEqual(1, (end_time - start_time).seconds)
        self.assertEqual('data', data)

    def test_get_timeout(self):
        q = queue.Queue()
        with self.assertRaises(_queue.Empty) as context:
            start_time = datetime.now()
            q.get(timeout=1)
        end_time = datetime.now()
        self.assertEqual(1, (end_time - start_time).seconds)
        self.assertEqual(0, len(context.exception.args))

    def test_get_no_blocking(self):
        q = queue.Queue()
        with self.assertRaises(_queue.Empty) as context:
            start_time = datetime.now()
            q.get(block=False)
        end_time = datetime.now()
        self.assertEqual(0, (end_time - start_time).seconds)
        self.assertEqual(0, len(context.exception.args))

    def test_get_nowait(self):
        q = queue.Queue()
        with self.assertRaises(_queue.Empty) as context:
            start_time = datetime.now()
            q.get_nowait()
        end_time = datetime.now()
        self.assertEqual(0, (end_time - start_time).seconds)
        self.assertEqual(0, len(context.exception.args))

    def test_task_done_put(self):
        q = queue.Queue()

        def worker():
            q.put('data')
            time.sleep(2)  # put/get should go first
            q.task_done()

        t = threading.Thread(target=worker, daemon=True)
        start_time = datetime.now()
        t.start()

        q.join()
        end_time = datetime.now()
        self.assertEqual(2, (end_time - start_time).seconds)
        self.assertEqual('data', q.get())

    def test_task_done_get(self):
        q = queue.Queue()

        def worker():
            q.get()
            q.task_done()

        t = threading.Thread(target=worker, daemon=True)
        t.start()

        q.put('data')
        self.assertEqual(1, q.qsize())
        q.join()
        self.assertEqual(0, q.qsize())


if __name__ == '__main__':
    unittest.main()
