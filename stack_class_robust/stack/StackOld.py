
class Stack:

    def __init__(self):
        self.items = []
        self.size = 0 
    
    
    def isEmpty(self):
        return self.size == 0
    

    def peek(self):
        return self.items[self.size - 1]

    def pop(self):
        self.size -=1
        return self.items.pop()
    
    def push(self, item):
        self.items.append(item)
        self.size +=1
    
    def sizeOf(self):
        return self.size

    
    



    