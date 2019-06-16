# Node class of Doubly linked list
class Node:
    
    # Function to initialise the data, next pointer and the prev pointer 
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Doubly linked list class

class DoublyLinkedList:

    # Function to initialise the doubly linked list
    def __init__(self):
        self.head = None
    
    # Function to add a new_node in the front of doubly_linked_list
    def push(self, data):
        
        # create the new_node
        node = Node(data)
        
        # check if the DLL is empty or not
        if self.head is None:
            self.head = node
            return

        # point the next of the node to the head of DLL
        node.next = self.head
        # point the prev of the head node to the new_node
        self.head.prev = node
        # point the head of the DLL to the new node
        self.head = node

    # Function to add a new_node after a particular node in doubly_linked_list
    def insert_after(self, prev_node, data):
        
        # check if the prev_node is null
        if prev_node is None:
            print("This node does not exist in DLL")
            return
        # create the new_node
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        # store the address of the next node of prev_node in a temp variable
        temp = prev_node.next 
        # point the next of prev_node to this new_node
        prev_node.next = new_node
        # point the next of new_node to the temp variable
        new_node.next = temp

        # point the prev of new_node to the prev_node
        new_node.prev = prev_node

        # check if the next of new_node is None
        if new_node.next is not None:
            new_node.next.prev = new_node
    
    # Function to add a new_node before a particular node in doubly_linked_list
    def insert_before(self, after_node, data):

        # create a new_node
        new_node = Node(data)

        # check if the after_node actually exists
        if self.head is None:
            print("The after_node does not exist in the doubly linked list")
            return

        # save the prev_node of after_node in a temp var
        temp = after_node.prev

        # point the prev of after_node to the new_node
        after_node.prev = new_node

        # point the next of new_node to the after_node
        new_node.next = after_node

        # point the prev of new_node to temp
        new_node.prev = temp

        # check if the prev of new_node is null
        if new_node.prev is not None:
            new_node.prev.next = new_node
        
        if self.head == after_node:
            self.head = new_node
    

    # Function add a new_node to the end
    def append(self, data):

        # create a new_node
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # initialise the pointer to reach the last node
        last_node = self.head

        while(last_node.next):
            last_node = last_node.next
        
        last_node.next = new_node
        new_node.prev = last_node
    
    # function to print the doubky linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":

    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)

    dll.print_list()

    dll.insert_after(dll.head, 7)
    dll.print_list()

    dll.insert_before(dll.head, 8)
    dll.print_list()