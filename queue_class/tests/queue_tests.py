
import unittest
import sys
sys.path.insert(0, './queue')
from Queue import Queue
from Node import Node



class TestNode(unittest.TestCase):
    def setUp(self):
        self.our_node = Node(10)
    
    def test_get_data(self):
        self.assertEqual(10, self.our_node.getData())
    

    def test_set_data(self):
        self.assertEqual(10, self.our_node.getData())
        self.our_node.setData(5)
        self.assertEqual(5, self.our_node.getData())

    

    def test_get_next_node(self):
        new_node = Node(6)
        self.our_node.setNextNode(new_node)
        self.assertEqual(self.our_node.getNextNode(), new_node)
    

    




class TestQueue(unittest.TestCase):
    def setUp(self):
        self.our_queue = Queue()

    def test_is_empty(self):
        self.assertTrue(self.our_queue.isEmpty())


    def test_enqueue(self):
        self.our_queue.enqueue(5)
        self.assertEqual(5, self.our_queue.peek())

    
    def test_is_not_empty(self):
        self.our_queue.enqueue(5)
        self.assertFalse(self.our_queue.isEmpty())
    

    def test_dequeue(self):
        self.our_queue.enqueue(5)
        self.our_queue.enqueue(8)
        self.our_queue.enqueue(5)
        self.assertEqual(5, self.our_queue.peek())
        self.assertEqual(5, self.our_queue.dequeue())
        self.assertEqual(8, self.our_queue.peek())
    

    def test_get_size(self):
        self.our_queue.enqueue(5)
        self.our_queue.enqueue(8)
        self.our_queue.enqueue(5)
        self.assertEqual(3, self.our_queue.sizeOf())




    

    
    



    


if __name__ == '__main__':
    unittest.main()