"""Delete the nth node from last by single pass"""
# A Node for linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
# a linked list class
class LinkedList:
    def __init__(self):
        self.head = None
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
    def print_list(self):
        mover = self.head
        while(mover):
            print(mover.val, end=" ")
            mover = mover.next
        print()
def remover_last_n(l1, n):
    first_mover = l1
    follower_mover = l1
    # delay the follower_mover by n
    while(n):
        first_mover = first_mover.next
        n = n-1
    if not first_mover:
        l1 = l1.next
        return l1
    while(first_mover.next):
        first_mover = first_mover.next
        follower_mover = follower_mover.next
    follower_mover.next = follower_mover.next.next
    return l1

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.print_list()
    ll = remover_last_n(ll.head, 5)
    while(ll):
        print(ll.val, end=" ")
        ll = ll.next
    print()



