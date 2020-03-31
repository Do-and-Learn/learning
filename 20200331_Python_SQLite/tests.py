import sqlite3
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.conn = sqlite3.connect(':memory:')  # or test.db will create db file

    def tearDown(self) -> None:
        self.conn.close()

    def test_something(self):
        c = self.conn.cursor()
        c.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")

        rows = c.execute('SELECT * FROM stocks ORDER BY price')
        self.assertEqual(0, len([row for row in rows]))

    def test_something2(self):
        c = self.conn.cursor()
        c.execute("CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")

        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
        self.conn.commit()

        rows = c.execute('SELECT * FROM stocks ORDER BY price')
        self.assertEqual(3, len([row for row in rows]))


if __name__ == '__main__':
    unittest.main()
