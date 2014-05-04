import unittest
from queue import Queue

class TestQueueFunctions(unittest.TestCase):

    def test_fetched_item_equals_last_inserted_item(self):
        queue = Queue()
        queue.put(18)
        self.assertEqual(queue.get(), 18)

if __name__ == '__main__':
    unittest.main()