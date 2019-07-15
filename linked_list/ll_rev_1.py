"""Reverse the linked list (practice_1) """
# class for a linked list
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Linked List class
class LinkedList:

    # initilise the head of the linked list
    def __init__(self):
        self.head = None
    
    # add a node in the ned of linked list
    def add_node(self, data):
        
        # create a new node to add data
        new_node = Node(data)
        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
            return
        # mover to reach the last node
        mover = self.head
        # reach the end of the linked list
        while(mover.next):
            mover = mover.next
        # add the new node at the end
        mover.next = new_node
    
    def reverse_ll(self):

        # check if the ll is valid
        if self.head is None:
            return
        
        curr_node = self.head
        next_node = curr_node.next
        # prev_node is Null becauase this node is last node
        # of the reversed_ll
        prev_node = None
        # reverse till the second last node
        while(curr_node.next):
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next
        
        curr_node.next = prev_node
        self.head = curr_node
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
if __name__ == "__main__":
    
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)
    # print the original list
    ll.print_list()
    ll.reverse_ll()
    # print the reversed list
    ll.print_list()