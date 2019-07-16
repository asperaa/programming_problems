"""Reverse a linked list (practice 2) """
# class for a node
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# class for a linked list
class LinkedList:
    # initialise the head of the linkedlist
    def __init__(self):
        self.head = None
    
    # function to add a new node at the start of the linked list
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # reverse the linked list
    def reverse(self):
        # check if the linked list is empty
        if self.head is None:
            return
        current_node = self.head
        next_node = None
        prev_node = None

        while(current_node):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    
    # function to print a new node
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(8)
    ll.add_front(7)
    ll.add_front(6)
    ll.add_front(5)
    ll.add_front(4)
    ll.add_front(3)
    # print the list before the reversal
    ll.print_list()
    ll.reverse()
    # print the list after the reversal
    ll.print_list()
