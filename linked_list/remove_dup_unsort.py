"""RemNoove duplicates from an unsorted linked list"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    
    def __init__(self):
        self.head = None
    # add a new node to the front of ll
    def add_front(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    # print the linked list
    def print_List(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    # remove duplicates from an unsorted list
    def remove_dup(self):

        # check if the ll is empty
        def 