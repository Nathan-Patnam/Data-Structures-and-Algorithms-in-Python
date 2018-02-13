from Node import Node
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def dequeue(self):
        temp = self.head
        if self.size ==1:
            self.head = None
            self.tail - None
        else:
            self.head = self.head.getNextNode()
        self.size-=1
        return temp.getData()


    def enqueue(self, item):
        temp = Node(item)
        if self.isEmpty():
            self.head = temp
            self.tail = temp
        if self.size == 1:
            self.head.setNextNode(temp)
            self.tail = temp
        else:
            self.tail.setNextNode(temp)
            self.tail = temp
        self.size+=1

        


    def isEmpty(self):
        return self.size == 0
        
    
    def peek(self):
        return self.head.getData()
        
    
    def sizeOf(self):
        return self.size
        

    
    



    