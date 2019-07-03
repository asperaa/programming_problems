"""Rotate the ll counter clock wise by n nodes """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    
    # add a node to the end of linked list
    def __init__(self):
        self.head = None
    
    # add a node to the front of linked list
    def add_front(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    # print a linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    
    # rotate a linked list by k node in counter clock wise direction
    def rotate(self, k):
        # check if the ll is empty
        if self.head is None:
            return
        
        counter = 0
        mover = self.head
        prev = self.head
        while(mover and counter != k):
            counter += 1
            prev = mover
            mover = mover.next
        # mark the next of last node of the new ll as None
        prev.next = None 
        # save the new head of the linked list
        new_head = mover
        # reach the last node of the current linked list
        while(mover.next):
            mover = mover.next
        # next of the last node of current ll to the head of current ll
        mover.next = self.head
        self.head = new_head
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(60)
    ll.add_front(50)
    ll.add_front(40)
    ll.add_front(30)
    ll.add_front(20)
    ll.add_front(10)

    ll.print_list()

    ll.rotate(4)

    ll.print_list()