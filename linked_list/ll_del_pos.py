# class for a Node
class Node:

    # function to initialise a node
    def __init__(self, data):
        self.data = data
        self.next = None


# class for linked list
class LinkedList:

    # function to initialise a node
    def __init__(self):
        self.head = None
    
    # function to add a new_node in start
    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head= new_node
    
    # function to delete a node a particular postion (starts from 0)
    def delete(self, pos):
        
        # initialise the pointer
        temp = self.head
        # initialise the counter of position
        count = 0

        # find the position in ll
        while(temp is not None and count != pos):
            count = count + 1
            prev = temp
            temp = temp.next
        
        # check if the ll is too small
        if temp is None:
            print("Linked list is too small")
            return
        
        # check if the position is head of ll
        if count == 0:
            self.head = temp.next
            temp = None
            return
        # change the pointers to remove the links
        prev.next = temp.next
        
        # point the intended node to None
        temp = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
            


if __name__ == '__main__':

    ll = LinkedList()
    ll.push(2)
    ll.push(4)
    ll.push(5)
    ll.push(10)

    ll.print_list()
    ll.delete(2)

    ll.print_list()

    ll.delete(0)
    ll.print_list() 
    ll.delete(8)       
        
            

    