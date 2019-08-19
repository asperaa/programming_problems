"""Reorder the linked list like: L0->L1->L2.....Ln-1->Ln to L0->Ln->L2->Ln-2->Ln-3"""
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
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def reverse(self, head):
        prev_node = None
        curr_node = head
        next_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head

    def re_order(self):
        slow_ptr = self.head
        fast_ptr = self.head
        prev_mid = None
        while slow_ptr and fast_ptr and fast_ptr.next:
            prev_mid = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        prev_mid.next = None
        l1_mover = self.head
        l2_mover = self.reverse(slow_ptr)

        while l1_mover.next:
            next_l1 = l1_mover.next
            next_l2 = l2_mover.next
            l1_mover.next = l2_mover
            l2_mover.next = next_l1
            l1_mover = next_l1
            l2_mover = next_l2
        
        if l2_mover:
            l1_mover.next = l2_mover
        
        return l1_mover

        
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    # ll.append(5)
    ll.print_list()
    ll.re_order()
    ll.print_list()

