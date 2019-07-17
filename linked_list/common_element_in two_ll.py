"""find the first common elment in two linked list 
   i.e find the first node of the first list which is
   also present in the second list"""
# Node class
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    # inilialise the head of the ll
    def __init__(self):
        self.head = None
    
    # add a new node to the end of the linked list
    def add_end(self, data):
        # create a new node
        new_node = Node(data)
        # check if the ll is empty
        if self.head is None:
            self.head = new_node
            return
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
    
    # function to find the first common element in linked list

    
    # function to print the list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

def find_common(l1, l2):
    s = set()
    mover = l2.head
    while(mover):
        s.add(mover.data)
        mover = mover.next
    mover = l1.head
    while(mover):
        if mover.data in s:
            return mover.data
    
    return

if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_end(10)
    l1.add_end(15)
    l1.add_end(4)
    l1.add_end(20)

    l2 = LinkedList()
    l2.add_end(8)
    l2.add_end(4)
    l2.add_end(12)
    l2.add_end(10)

    print(find_common(l1, l2))
