"""Swap the data of the ll pair-wise"""
# Node class
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data # fill the data in the data filed
        self.next = None # point the next of node to null

# linked list class
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    
    # add a new node to the front of linked list
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        # check if the new node of the class is empty
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # print the list of print_list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
        
    # function to pair-wise swap the linked list
    def pair_wise(self):

        curr_node = self.head
        while(curr_node and curr_node.next):
            temp = curr_node.data 
            curr_node.data = curr_node.next.data
            curr_node.next.data = temp
            curr_node = curr_node.next.next
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(1)
    ll.add_front(2)
    ll.add_front(3)
    ll.add_front(4)
    ll.add_front(5)
    ll.add_front(6)
    # ll.add_front(7)

    ll.print_list()

    ll.pair_wise()

    ll.print_list()





