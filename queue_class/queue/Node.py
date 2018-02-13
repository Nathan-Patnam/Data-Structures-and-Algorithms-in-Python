class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        
    def getData(self):
        return self.value
    
    def setData(self, value):
        self.value = value
    
    def getNextNode(self):
        return self.next

    def setNextNode(self, node):
        self.next = node

