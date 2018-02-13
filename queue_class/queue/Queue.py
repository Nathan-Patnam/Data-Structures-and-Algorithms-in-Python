from Node import Node
class Queue:

    def __init__(self):
        self.__set_tail_and_head(None, None)
        self.size = 0
     

    def dequeue(self):
        temp_data = self.head.get_data() 
        if self.size ==1:
            self.__set_tail_and_head(None, None)
        else:
            self.head = self.head.get_next_node()
        self.size-=1
        return temp_data
            


    def enqueue(self, item):
        temp = Node(item)
        if self.is_empty():
            self.__set_tail_and_head(temp, temp)
        else:
            self.tail.set_next_node(temp)
            self.tail = temp
        self.size+=1
    
    def __set_tail_and_head(self,tail, head):
        self.head = head
        self.tail = tail
            


    def is_empty(self):
        return self.size == 0
        
    
    def peek(self):
        return self.head.get_data()
        

    def size_of(self):
        return self.size

    
    



    