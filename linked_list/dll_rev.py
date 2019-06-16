# dll node class
class Node:

    # function to initialise the node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# class for doubly_linked_list
class DoublyLinkedList:
    
    # initialise the head
    def __init__(self):
        self.head = None
    
    # append a new_node
    def append(self, data):

        # create a new_node
        new_node = Node(data)
        
        # check if DLL is empty
        if self.head is None:
            self.head = new_node
            return

        # temp_node to reach the last node
        last_node = self.head

        # reach the last node
        while(last_node.next):
           last_node = last_node.next
        
        # point the next of last node to the new node
        last_node.next = new_node
        new_node.prev = last_node

    
    def reverse(self):

        # check if DLL is empty
        if self.head is None:
            self.head = None
            return
        
        # to reach the end of DLL
        mover = self.head
  
        while(mover.next):
            # saving the next_node
            temp = mover.next
            # changing the next of mover_node to prev of mover_node
            mover.next = mover.prev
            # changing the prev of mover to next
            mover.prev = temp
            # moving the mover ahead
            mover = temp
        
        # make the head the last node
        mover.next = mover.prev
        mover.prev = None
        self.head = mover
    
    def print_list(self):

        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    

if __name__ == "__main__":

    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)

    dll.print_list()

    dll.reverse()

    dll.print_list()
    
