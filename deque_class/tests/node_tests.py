import unittest
import sys
sys.path.insert(0, '.././deque')
from Node import Node



class TestNode(unittest.TestCase):
    def setUp(self):
        self.our_node = Node(10)
    
    def test_get_data(self):
        self.assertEqual(10, self.our_node.get_data())
    

    def test_set_data(self):
        self.assertEqual(10, self.our_node.get_data())
        self.our_node.set_data(5)
        self.assertEqual(5, self.our_node.get_data())

    

    def test_get_next_node(self):
        new_node = Node(6)
        self.our_node.set_next_node(new_node)
        self.assertEqual(self.our_node.get_next_node(), new_node)

if __name__ == '__main__':
    unittest.main()