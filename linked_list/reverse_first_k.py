"""Reverse the first k elements of the linked list"""
# Node class for each node of the linked list
class Node:
    # initialise the node with the data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    # initialise the head of the class
    def __init__(self):
        self.head = None
    
    # add a node to the front of the linked list
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    # function to reverse first k nodes of the linked list
    def reverse_frist_k(self, k):
        # check if the ll is empty
        if self.head is None:
            return
        
        current_node = self.head
        next_node = None
        prev_node = None
        count = 0

        while(current_node and count < k):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            count += 1
        # point the next of the original first node 
        # to the first node of the un-reversed ll
        self.head.next = next_node
        # change the head of the linked list to 
        # point to the new node (first node of reversed part of ll)
        self.head = prev_node
    
    # print the linke the linked list
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
    ll.add_front(2)
    ll.add_front(1)
    # print the original linked list
    ll.print_list()
    # reverse the linked list
    ll.reverse_frist_k(5)
    # print the reversed linked list
    ll.print_list()
        
