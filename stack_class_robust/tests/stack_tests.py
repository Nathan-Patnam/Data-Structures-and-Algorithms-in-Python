
import unittest

import sys
sys.path.insert(0, '.././stack')
from Stack import *



class TestStack(unittest.TestCase):
    def setUp(self):
        self.our_stack = Stack()

    def test_stack_created(self):
        self.assertTrue(self.our_stack.is_empty())
    
    def test_get_capcity(self):
        self.assertEquals(10, self.our_stack.get_capacity())

    def test_set_capacity(self):
        self.small_stack = Stack(3)
        self.assertEquals(3, self.small_stack.get_capacity())

    def test_add_item(self):
        self.our_stack.push(3)
        self.assertEqual(3, self.our_stack.peek())
    
    def test_remove_item_from_emtpy_stack(self):
        with self.assertRaises(RuntimeError):
            self.our_stack.pop()
        
    
    def test_peek_in_empty_stack(self):
        with self.assertRaises(RuntimeError):
            self.our_stack.peek()
    
    def test_remove_item(self):
        self.our_stack.push(6)
        self.our_stack.push(4)
        self.our_stack.push(9)
        self.assertEqual(9, self.our_stack.pop())
        self.assertEqual(4, self.our_stack.peek())

    def test_get_size(self):
        self.our_stack.push(6)
        self.our_stack.push(4)
        self.our_stack.push(9)
        self.assertEqual(3, self.our_stack.size_of())
    
    def test_extend_array(self):
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.our_stack.push(6)
        self.assertEqual(11, self.our_stack.size_of())
    



    


if __name__ == '__main__':
    unittest.main()