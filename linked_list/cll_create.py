# class for Circular linked list node
class Node:

    # function to initiate a new_node
    def __init__(self, data):
        self.data = data
        self.next = None

# class for circular linked list
class CircularLinkedList:

    # function to initialise the new_node
    def __init__(self):
        self.head = None
    
    # function to push data in the front of circular linked list
    def push(self, data):
        
        # create a new node
        new_node = Node(data)
        # point next of new_node to head of CLL
        new_node.next = self.head
        
        # temp variable as a mover
        temp = self.head
        
        # CLL is not empty
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node     
        else:
            new_node.next = new_node

        self.head = new_node

    # function to print a circular linked list
    def print_list(self):
        temp = self.head
        while(True):
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()

if __name__ == "__main__":

    dll = CircularLinkedList()
    dll.push(10)
    dll.push(9)
    dll.push(8)
    dll.push(7)
    dll.push(6)
    
    dll.print_list()

        
        
