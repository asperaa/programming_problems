"""Segregate odd nodea and evene nodes"""
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

    def print_list(self):
        mover = self.head
        count = 0
        while(mover):
            print(mover.val, end=" ")
            mover = mover.next
            count += 1
            if count == 6:
                break
        print()
    
    def odd_even(self):
        if not self.head:
            return
        odd_start = self.head
        prev_odd = self.head
        even_start = self.head.next
        even_head = self.head.next

        while odd_start and even_start and odd_start.next and even_start.next:
            prev_odd = odd_start
            odd_start.next = odd_start.next.next
            even_start.next = even_start.next.next
            odd_start = odd_start.next
            even_start = even_start.next

        if odd_start:
            odd_start.next = even_head
        else:
            prev_odd.next = even_head
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.odd_even()
    ll.print_list()