"""Detect the cycle in a linked list in constant space"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = ListNode(val)
            return
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
        return
    # Slow ptr and fast ptr approach. Same as middle of the linked list..
    def detect(self):

        first_mover = self.head # slow ptr
        second_mover  = self.head # fast ptr
        
        # keep moving the slow and fast ptr
        # when they are in the loop they will eventually meet 
        while(second_mover and second_mover.next):
            first_mover = first_mover.next
            second_mover = second_mover.next.next
            # condition for when the fast and slow ptr overlap
            if first_mover == second_mover:
                return True
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
    ll.append(8)
    
    ll.head.next.next.next.next.next.next.next.next = ll.head.next.next

    print(ll.detect())