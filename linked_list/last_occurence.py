"""delete the last occurence of an item from the linked list"""
import gc

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, data):
        
        # create a new node 
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    
    def del_last_occur(self, data):
        
        # check if the linked list is empty
        if self.head is None:
            return
        
        mover = self.head
        last = self.head

        while(mover):
            if mover.data == data:
                last = mover
            mover = mover.next
        
        mover = self.head
        while(mover.next != last):
            mover = mover.next
        mover.next = mover.next.next
        
        last.next = None
        
        gc.collect()
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(3)
    # ll.append(5)

    ll.print_list()

    ll.del_last_occur(3)

    ll.print_list()



