# Node class
class Node:
    
    # Function to initialise the node
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialise next as None

# Linked List class
class LinkedList:
    # Function to initialise the node
    def __init__(self):
        self.head = None # Initialse the head as None

   
    # Function to push the new node in the front of linked list
    def push(self, data):
        
        # create a new node
        new_node = Node(data)

        # point the next of new_node to the head of linked list
        new_node.next = self.head
        
        # change the head of the new node
        self.head = new_node

        return self.head
    
    
    # Function to push the new node after a particular node in linked list
    def insertAfter(self, prev_node, data):
        
        # check if the previous node is null
        if prev_node == None:
            print("The previous node is not in a linked list")
            return

        # create a new node and put in the data
        new_node = Node(data)

        # point the pointer of the new_node to the next of the previous_node
        new_node.next = prev_node.next
        
        # point the pointer of the prev_node towards the new node
        prev_node.next = new_node

    
    # Function to append in the end of the linked list
    def append(self, data):
        
        # create a new_node and insert data and set the next of this node as null
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        
        # initialise the last_pointer to point towards the head
        last_ptr = self.head

        # reach the the end of the linked list
        while(last_ptr.next!= None):
            last_ptr = last_ptr.next

        # point the next of the last_pte towards the new node
        last_ptr.next = new_node

    
    def print_list(self):

        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.push(7)
    linked_list.append(9)

    linked_list.insertAfter(linked_list.head.next, 10)
    linked_list.print_list()

        
        



        
    