"""Reverse list of K member groups"""
class Node:
    # initialise the data
    def __init__(self, data):
        self.data = data
        self.next = None
# Linked list class
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None

    # function to add a new node at the front
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # function to print the ll
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def reverse_k_groups(self, temp_head, k):
        # check if the linked list is empty
        if self.head is None:
            return
        
        current_node = temp_head
        next_node = None
        prev_node = None
        count = 0
        while(current_node and count < k):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            count += 1
        
        if next_node is not None:
            temp_head.next = self.reverse_k_groups(next_node, k)
        # keep updated the head of the ll
        self.head=prev_node
        # prev_node is the head of the input linked list
        return prev_node

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(8)
    ll.add_front(7)
    ll.add_front(6)
    ll.add_front(5)
    ll.add_front(4)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)

    ll.print_list()
    ll.reverse_k_groups(ll.head, 4)
    ll.print_list()