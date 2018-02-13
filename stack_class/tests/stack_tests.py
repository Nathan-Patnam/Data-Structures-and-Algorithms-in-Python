
import unittest

import sys
sys.path.insert(0, './stack')
import Stack



class TestStack(unittest.TestCase):
    def setUp(self):
        self.our_stack = Stack.Stack()

    def test_stack_created(self):
    
        self.assertTrue(self.our_stack.isEmpty())
    
    def test_add_item(self):
        self.our_stack.push(3)
        self.assertEqual(3, self.our_stack.peek())
    
    def test_remove_item(self):
        self.our_stack.push(6)
        self.our_stack.push(4)
        self.our_stack.push(9)
        self.assertEqual(9, self.our_stack.peek())
        self.assertEqual(9, self.our_stack.pop())
        self.assertEqual(4, self.our_stack.peek())

    
    def test_get_size(self):
        self.our_stack.push(6)
        self.our_stack.push(4)
        self.our_stack.push(9)
        self.assertEqual(3, self.our_stack.sizeOf())
    



    


if __name__ == '__main__':
    unittest.main()