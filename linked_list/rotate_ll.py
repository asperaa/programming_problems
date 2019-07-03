"""Rotate the ll counter clock wise by n nodes """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add_front(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
