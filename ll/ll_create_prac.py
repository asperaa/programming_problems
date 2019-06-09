# Class for Node
class Node:
    
    # function to initialise the node
    def __init__(self, data):
        self.data = data     # adding data to the node
        self.next = None     # pointing the next of node to null

# class for linked list data structure
class LinkedList:

    # function to initialise a linked list
    def __init__(self):
        self.head = None # putting the next of head of linked list to null
    
    # function to add a node to the beginning of the linked list
    def push(self, data):


        # create a new_node and fill it with data
        new_node = Node(data)
        
        # change the next of the new_node to point towards the head of the linked list
        new_node.next = self.head

        # change the head of the linked list to the new_node
        self.head = new_node

    # function to add a node after a particular node
    def insert_after(self, prev_node, data):
        
        # check whether the prev_node is null or not
        if prev_node is None:
            print("The given previous node is not a part of linked list")
            return
        # create a new_node and fill it
        new_node = Node(data)
        
        # point the next of new_node to the next of prev_node
        new_node.next = prev_node.next

        # point the next of prev_node to the next of new_node
        prev_node.next = new_node

    
    # function to add a node at the end of the linked_list
    def append(self, data):

        # create a new_node and fill it with data
        new_node = Node(data)

        # check whether a linked list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # get the pointer to the last node of the linked list
        last = self.head
        while(last.next):
            last = last.next
        
        # point the next of the last_node to new_node
        last.next = new_node
    
    # function to print the list
    def print_list(self):

        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    


if __name__ == "__main__":
    
    ll = LinkedList()

    ll.push(8)
    ll.push(9)
    ll.append(10)

    ll.insert_after(ll.head.next.next, 80)

    ll.print_list()
    