
import unittest
import sys
sys.path.insert(0, '.././deque')
from Deque import Deque


class TestDeque(unittest.TestCase):
    def setUp(self):
        self.our_deque = Deque()

    def test_is_empty(self):
        self.assertTrue(self.our_deque.is_empty())


    def test_add_front(self):
        self.our_deque.add_first(5)
        self.assertEqual(5, self.our_deque.peek_first())
    
    def test_insert_rear(self):
        self.our_deque.add_last(5)
        self.assertEqual(5, self.our_deque.peek_first())

    
    def test_is_not_empty(self):
        self.our_deque.add_first(5)
        self.our_deque.add_last(8)
        self.assertFalse(self.our_deque.is_empty())
    

    def test_remove_front(self):
        self.our_deque.add_first(7)
        self.our_deque.add_last(8)
        self.our_deque.add_last(5)
        self.assertEqual(7, self.our_deque.peek_first())
        self.assertEqual(7, self.our_deque.remove_front())
        self.assertEqual(8, self.our_deque.peek_first())
    
    def test_remove_rear(self):
        self.our_deque.add_first(7)
        self.our_deque.add_first(8)
        self.our_deque.add_first(5)
        self.assertEqual(7, self.our_deque.peek_last())
        self.assertEqual(7, self.our_deque.remove_rear())
        self.assertEqual(8, self.our_deque.peek_last())
    


    def test_get_size(self):
        self.our_deque.add_first(5)
        self.our_deque.add_last(8)
        self.our_deque.add_first(5)
        self.assertEqual(3, self.our_deque.size_of())

if __name__ == '__main__':
    unittest.main()