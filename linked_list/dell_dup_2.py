"""Delete the duplicates in ll and only keep distinct elments at the end"""
# A Node class
class Node:
    # initialse the node with data and next
    def __init__(self, data):
        self.data = data
        self.next = None
# A linked list class
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    # function to add new node to the end of linked list
    def append(self, data):
        # make a new node
        new_node = Node(data)
        # check if the ll is empty
        if not self.head:
            self.head = new_node
            return
        # pointer to move to the end of the linked list
        mover = self.head
        # move to theend of the linked list
        while(mover.next):
            mover = mover.next
        # attach the node to the end of linked list
        mover.next = new_node
        return
    # print the list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def delete_dup(self):
        if not self.head:
            return
        # assign the prev and next node    
        prev = self.head
        curr = prev.next
        # flag to check if the first few elements are duplicates
        first_dup = 0
        if self.head.next and self.head.data == self.head.next.data:
            first_dup = 1 

        while(curr and curr.next):
            if curr.data == curr.next.data:
                while(curr and curr.next and curr.data == curr.next.data):
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        # handle the case of first element 
        # of the linked list having a duplicate
        if first_dup:
            if self.head.next and self.head.data == self.head.next.data:
                self.head = self.head.next.next
            elif self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(1)
    ll.append(1)
    ll.append(3)
    ll.append(3)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.print_list()
    ll.delete_dup()
    ll.print_list()
