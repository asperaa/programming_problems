"""Detect cylce in a linked list"""
class ListNode:
    # initialise the node with data and next pointer
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    # function to add a new node to the end of the linked list 
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
        return
    # function to print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()
    # function to detect the cycle
    # use hash set to store the consective nodes
    # if the nodes. If cycle, 
    # then duplicate nodes are found in hash set 
    def detect(self):
        hash_set = set()
        if not self.head:
            return
        mover = self.head
        while(mover):
            if not mover in hash_set:
                hash_set.add(mover)
            else:
                return True
            mover = mover.next
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    
    ll.print_list()
    ll.head.next.next.next.next.next.next.next = ll.head.next.next
    print(ll.detect())
