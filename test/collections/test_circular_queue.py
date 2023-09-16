import unittest

from optimal.collections.circular_queue import CircularQueue


class TestCircularQueue(unittest.TestCase):
    def setUp(self):
        pass

    def test_populate_with_append(self):
        q = CircularQueue(3)
        q.append(4)
        assert q.get_data() == [4, None, None]
        q.append(5)
        assert q.get_data() == [5, 4, None]
        q.append(6)
        assert q.get_data() == [6, 5, 4]
        q.append(7)
        assert q.get_data() == [7, 6, 5]

        assert q.first() == 5
        assert q.last() == 7
