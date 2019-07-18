"""Pair wise swap of nodes of all in a simple appraoch"""
class Node:
    # initialise the node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # initialise the head of linked list
    def __init__(self):
        self.head = None
    
    # add a new node at the end of linked list
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # print the list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    # function to pair-wise swap the the things
    def pair_wise(self, temp_head):
        # check if the ll has less than 2 nodes
        if temp_head is None or temp_head.next is None:
            return temp_head
        
        # store the head of the ll after first two nodes of the current ll
        remaining = temp_head.next.next
        # store the new head
        new_head = temp_head.next
        # change the next of the second node of the current linked list
        temp_head.next.next = temp_head
        # recur for remaing list and change next of head
        temp_head.next = self.pair_wise(remaining)
        self.head = new_head
        return new_head


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(1)
    ll.add_front(2)
    ll.add_front(3)
    ll.add_front(4)
    ll.add_front(5)

    ll.print_list()

    ll.pair_wise(ll.head)
    ll.print_list()
