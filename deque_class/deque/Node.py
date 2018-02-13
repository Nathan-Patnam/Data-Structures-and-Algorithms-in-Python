
class Node:
    def __init__(self, value):
        self.next = None
        self.value = value
        
    def get_data(self):
        return self.value
    
    def set_data(self, value):
        self.value = value
    
    def get_next_node(self):
        return self.next

    def set_next_node(self, node):
        self.next = node

