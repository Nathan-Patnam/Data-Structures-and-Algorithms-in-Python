from Node import Node
class Deque:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_first(self,item):
        temp = Node(item)
        if self.is_empty():
            self.__set_head_tail_same_value(temp)
        else:
            temp.set_next_node(self.head)
            self.head = temp
        self.size+=1


    def add_last(self, item):
        temp = Node(item)
        if self.is_empty():
            self.__set_head_tail_same_value(temp)
        else:
            self.tail.set_next_node(temp)
            self.tail = temp
        self.size+=1


    def remove_front(self):
        if self.size ==1:
            set_head_tail(None)
        else:
            temp = self.head
            self.head = self.head.get_next_node()
        self.size-=1
        return temp.get_data()
    

    def remove_rear(self):
        if self.size == 1:
            self.__set_head_tail_same_value(None)
        else:
            temp_data = self.tail.get_data()
            #update tail
            node_before_tail_reached = False
            temp = self.head
            while node_before_tail_reached != True:
                if temp.get_next_node() is self.tail:
                    node_before_tail_reached = True
                else:
                    temp = temp.get_next_node()
            self.tail = temp
            self.tail.set_next_node(None)
        self.size -=1
        return temp_data
        


    def __set_head_tail_same_value(self, value):
        self.head = value
        self.tail = value


    def is_empty(self):
        return self.size == 0
        
    def peek_first(self):
        return self.head.get_data()
    
    def peek_last(self):
        return self.tail.get_data()
        
    def size_of(self):
        return self.size