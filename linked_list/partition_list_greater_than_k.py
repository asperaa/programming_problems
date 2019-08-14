"""Partition the linked list into greater than and smaller than k"""
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
            self.head = new_node
            return
        mover = self.head
        while mover.next:
            mover = mover.next
        mover.next = new_node
        return

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def partition(self, x):
        if not self.head:
            return self.head

        small_head = None
        small_list = None
        large_head = None
        large_list = None
        mover = self.head
        # go opver the original list and put respective nodes into 
        # small and large buckets
        while mover:
            if mover.val < x:
                if not small_head:
                    small_list = mover
                    small_head = small_list
                else:
                    small_list.next = mover
                    small_list = small_list.next
            else:
                if not large_head:
                    large_list = mover
                    large_head = large_list
                else:
                    large_list.next = mover
                    large_list = large_list.next
            mover = mover.next
            # make the end of the large list NULL
            if large_list:
                large_list.next = None
            # case of elements smaller than x
            if small_head:
                small_list.next = large_head
                self.head = small_head
            else: # case in which there are no smaller elements than k
                self.head = large_head
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(3)
    ll.append(2)
    ll.append(5)
    ll.append(2)

    ll.print_list()
    ll.partition(3)
    ll.print_list()