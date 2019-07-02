# delete the middle of the node
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
        
        # check if the linkedlist is empty
        if self.head is None:
            self.head = new_node
            return
        
        # temp var to reach the end of the node
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    
    # function to delete the middle of the node
    def mid_del(self):

        # check if the node is empty
        if self.head is None:
            return
        
        # initialise two movers -- fast and slow
        fast_ptr = self.head
        slow_ptr = self.head
        prev_ptr = None

        while(fast_ptr and fast_ptr.next):
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        prev_ptr.next = prev_ptr.next.next
        slow_ptr.next = None

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
    ll.append(5)

    ll.print_list()

    ll.mid_del()

    ll.print_list()    

    ll.append(6)
    ll.append(7)

    ll.print_list()

    ll.mid_del()

    ll.print_list()