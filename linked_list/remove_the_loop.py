"""Remove the loop in the linked list"""
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
        while(mover.next):
            mover = mover.next
        mover.next = new_node
        return
    
    def remover_loop(self):
        slow_ptr = self.head
        fast_ptr = self.head
        # count the cycle_length
        cycle_length = 0
        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                slow_ptr = slow_ptr.next
                cycle_length += 1
                while(slow_ptr != fast_ptr):
                    slow_ptr = slow_ptr.next
                    cycle_length += 1
                break
        if cycle_length == 0:
            return None

        first_mover = self.head
        second_mover = self.head
        while(cycle_length):
            first_mover = first_mover.next
            cycle_length -= 1
        while(first_mover.next != second_mover.next):
            first_mover = first_mover.next
            second_mover = second_mover.next
        first_mover.next = None
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # ll.append(7)
    # ll.append(8)
    
    ll.print_list()
    ll.head.next.next.next.next.next.next = ll.head.next.next
    # ll.print_list()
    ll.remover_loop()

        
