"""merge nodes of the second ll at alternate positions of the first ll (in-place)"""
# node class
class Node:
    #  initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    # add a new node at the start of the ll
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        # check if the linked list is empty
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # print the list
    def print_List(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
# function to insert nodes of second ll 
# at alternate positions of the first ll
def merge_alternate(l1, l2):
    curr_l1 = l1.head
    curr_l2 = l2.head
    next_l1 = None
    next_l2 = None

    while(curr_l1 and curr_l2):
        next_l1 = curr_l1.next
        next_l2 = curr_l2.next
        curr_l1.next = curr_l2
        curr_l2.next = next_l1
        curr_l1 = next_l1
        curr_l2 = next_l2
    l2.head = curr_l2

    return l1, l2

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    l1.add_front(5)
    l1.add_front(7)
    l1.add_front(17)
    l1.add_front(13)
    l1.add_front(11)

    l2.add_front(12)
    l2.add_front(10)
    l2.add_front(2)
    l2.add_front(4)
    l2.add_front(6)
    l2.add_front(90)
    l2.add_front(50)
    
    l1.print_List()
    l2.print_List()

    new_l1, new_l2 = merge_alternate(l1, l2)

    new_l1.print_List()
    new_l2.print_List()