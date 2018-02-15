
class Stack:

    def __init__(self, capacity= 10):
        self.items = [None] * capacity
        self.size = 0
        self.capacity = capacity

    
    def peek(self):
        if self.is_empty():
            raise RuntimeError('peek method called on empty stack')
        return self.items[self.size - 1]


    def pop(self):
        if self.is_empty():
            raise RuntimeError('pop method called on empty stack')
        self.size-=1
        return self.items[self.size]
    
    
    def is_empty(self):
        return self.size == 0
      
    
    def push(self, item):
        if self.__is_full():
            self.__extend()
        self.items[self.size] = item
        self.size+=1
    
    def __is_full(self):
        return self.size == self.capacity
    
    def __extend(self):
        new_array = [None] * (self.capacity * 2)
        for i, item in enumerate(self.items):
            new_array[i] = item
        del self.items
        self.items = new_array
        self.capacity *= 2
 
    
    
    def size_of(self):
        return self.size
    
    
    def get_capacity(self):
        return self.capacity
      
    
    

    
    



    