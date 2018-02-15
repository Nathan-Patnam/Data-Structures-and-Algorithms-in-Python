from Node import Node
class LinkedList:
    def __init__(self):
        self.head  = None
        self.tail = None
        self.size = 0
    
    
    def add(self, index, item):
        if index > self.size + 1:
            raise IndexError
        else:
            node_being_added = Node(item)
            if self.is_empty():
                self.head = node_being_added
                self.tail = node_being_added
            elif self.size == 1:
                node_being_added.set_next_node(self.head)
                self.head = node_being_added
            else:
                temp = self.get_node(index-1)
                node_being_added.set_next_node = temp.get_next_node()
                temp.set_next_node(node_being_added)
            self.size += 1
    
    def add_first(self, item):
        self.add(0, item)

    
    def add_last(self, item):
        self.add(self.size, item)
    
    
    def clear():
        if self.size == 0:
            return
        else:
            node_iterator = self.head
            while node_iterator != None:
                node_iterator = node_iterator.get_next_node()
                del self.head
    
    
    def contains(self,item):
        return self.index_of(item) != -1
    

    def get(self, index):
        return self.get_node(index).get_data()
    

    def get_first(self):
        self.peek()

    
    def get_last(self):
        if self.is_empty():
            raise IndexError
        else:
            data = self.tail.get_data
            return data
    
    def index_of(self, item):
        if self.is_empty():
            raise IndexError
        else:
            node_iterator = self.head
            for i in range(self.get_size()):
                if node_iterator.get_data() == item:
                    return i
                else:
                    node_iterator = node_iterator.get_next_node()
        return -1


    
    def is_empty(self):
        return self.size == 0
    

    def peek(self):
        if self.is_empty():
            raise IndexError
        else:
            data = self.head.get_data()
            return data

    def pop(self):
        self.remove(self.size - 1)
    

    def remove(self, index = 0):
        if self.is_empty():
            raise RuntimeError
        else:
            if self.size == 1:
                temp_data = self.head.get_data()
                self.head = None
                self.tail = None
            else:
                temp_node = self.get_node(index - 1)
                temp_data = temp_node.get_data()
                del temp_node
            self.size -=1
            return temp_data

    def get_node(self, index): 
        if self.is_empty() or index > self.size:
            raise IndexError
        node_iterator = self.head
        for i in range(index):
            node_iterator.get_next_node()
        return node_iterator

    def size_of(self):
        return self.size

    def to_array(self):
        new_array = [None] * self.size
        node_iterator = self.head
        for i in range(self.size):
            new_array[i] = node_iterator.get_data()
            if self.size != i:
                node_iterator = node_iterator.get_next_node()
        return node_iterator
        


    
            