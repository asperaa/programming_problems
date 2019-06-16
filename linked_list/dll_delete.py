import gc
# DLL node class

class Node:

    # function to initialise the node
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

# DLL class
class DoublyLinkedList:

    # function to initialise the head of doubly linked list
    def __init__(self):
        self.head = None
    
    # function to to append a new node in the back
    def append(self, data):
        
        # create a new node and fill it with data
        new_node = Node(data=data)
        
        # check if the DLL is empty
        if self.head is None:
            self.head = new_node
            return

        # initialise the last node
        last_node = self.head
        
        # reach the last node
        while(last_node.next):
            last_node = last_node.next
        # poin the next of last node to the new_node
        last_node.next = new_node

        # point the prev of new_node to last_node
        new_node.prev = last_node
    
    
    # function to delete a node if the pointer to the node is given
    def delete_node(self, del_node):

        # base case
        if self.head is None or del_node is None:
            return

        # when the node to be deleted is head_node
        if self.head is del_node:
            self.head = del_node.next
                  
        # change the next only if the node to be deleted is NOT the last node
        if del_node.next is not None:
            del_node.next.prev = del_node.prev
        
        # change the prev only if the node to be deleted is NOT the head node
        if del_node.prev is not None:
            del_node.prev.next = del_node.next
        
        # free the memory occupied by del_node
        gc.collect()
    
    # print the doubly_linked_list
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
    
    upper_limit = input()
    for num in range(3, int(upper_limit)):
        dll.append(num)
    
    dll.print_list()
    
    # delete head_node
    dll.delete_node(dll.head)

    dll.print_list()
    
    # delete a node somewhere in the middle
    dll.delete_node(dll.head.next)

    dll.print_list()
    
    # delete last_node
    dll.delete_node(dll.head.next)

    dll.print_list()





        


