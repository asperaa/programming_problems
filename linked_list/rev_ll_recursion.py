"""Reverse a linked list using recusion """
# Node class
class Node:
    # initialse the node
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    # initialise the data
    def __init__(self):
        self.head = None
    
    # add a new node at the end
    def append(self, data):
        # create a new node
        new_node = Node(data)

        if self.head is None:
            self.head  = new_node
            return
        # pointer to move to the end of the ll    
        mover = self.head
        # reach the end of the node
        while(mover.next):
            mover = mover.next
        mover.next = new_node
    
    # print the function
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    # function to reverse the linked list
    def reverse(self, head):
        # base condition: if the head is null or 
        # next of head is null return node itself
        if not head or not head.next:
            return head
        # make the recursive call
        temp = self.reverse(head.next)
        # difficult to describe in text
        head.next.next = head 
        head.next = None
        # keep updating the new head
        self.head = temp
        return temp

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    
    ll.print_list()

    ll_new = ll.reverse(ll.head)

    ll.print_list()



        
        
