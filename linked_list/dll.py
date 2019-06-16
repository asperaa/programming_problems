# Node class
class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DLL:

    def __init__(self):
        self.head = None
    
    def push(self, data):
        
        # create the node and fill the data
        new_node = Node(data=data)

        # next of new_node is head of ll
        new_node.next = self.head

        # prev of new_node is None
        new_node.prev = None
        
        # set the prev of head of ll to new_node 
        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node
    
    def insertAfter(self, prev_node, data):
        pass