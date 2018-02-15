
import unittest
import sys
sys.path.insert(0, '.././queue')
from LinkedList import LinkedList
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
    

    




class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.our_linked_list = LinkedList()

    def test_is_empty(self):
        self.assertTrue(self.our_linked_list.is_empty())


    def test_add_first_empty_list(self):
        self.our_linked_list.add_first(5)
        self.assertEqual(5, self.our_linked_list.peek())
    
    def test_add_last_empty_list(self):
        self.our_linked_list.add_last(5)
        self.assertEqual(5, self.our_linked_list.peek())
    
    def test_add_first_as_second_element(self):
        self.our_linked_list.add_first(5)
        self.our_linked_list.add_first(9)
        self.assertEqual(9, self.our_linked_list.peek())
    

    def test_add_last_as_second_element(self):
        self.our_linked_list.add_last(5)
        self.assertEqual(5, self.our_linked_list.peek())
        self.our_linked_list.add_first(9)
    
    def test_add_out_of_bounds(self):
        self.assertRaises
        

    def test_is_not_empty(self):
        self.our_linked_list.add_first(3)
        self.assertFalse(self.our_linked_list.is_empty())
    

    def test_remove(self):
        self.our_linked_list.add_first(5)
        self.our_linked_list.add_last(8)
        self.our_linked_list.add_first(3)
        self.assertEqual(8, self.our_linked_list.peek())
        self.assertEqual(8, self.our_linked_list.remove())
        self.assertEqual(5, self.our_linked_list.peek())
    

    def test_pop(self):
        self.our_linked_list.add_first(5)
        self.assertEqual(5, self.our_linked_list.pop())
    

    def test_get_size(self):
        self.our_linked_list.add_first(5)
        self.our_linked_list.add_last(8)
        self.our_linked_list.add(1,5)
        self.assertEqual(3, self.our_linked_list.size_of())
    

    def test_create_array(self):
        self.our_linked_list.add_first(5)
        self.our_linked_list.add_last(8)
        self.our_linked_list.add(1,3)
        self.assertEqual([5,3,8], self.our_linked_list.to_array())





    

    
    



    


if __name__ == '__main__':
    unittest.main()