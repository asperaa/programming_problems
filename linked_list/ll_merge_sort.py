"""Merge sort in a linked list"""
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
    
    def merge(self, l1, l2):
        head = None
        mover_l1 = l1
        mover_l2 = l2
        mover_k = None
        while mover_l1 and mover_l2:
            if not head:
                if mover_l1.val <= mover_l2.val:
                    head = l1
                    mover_k = head
                    mover_l1 = mover_l1.next
                else:
                    head = l2
                    mover_k = l2
                    mover_l2 = mover_l2.next
            else:
                if mover_l1.val <= mover_l2.val:
                    mover_k.next = mover_l1
                    mover_l1 = mover_l1.next
                else:
                    mover_k.next = mover_l2
                    mover_l2 = mover_l2.next
                mover_k = mover_k.next
        
        while mover_l1:
            mover_k.next = mover_l1
            mover_l1 = mover_l1.next
            mover_k = mover_k.next

        while mover_l2:
            mover_k.next = mover_l2
            mover_l2 = mover_l2.next
            mover_k = mover_k.next
        
        return head

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        slow_ptr = head
        fast_ptr = head
        while slow_ptr and fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        # case of only two nodes in the linked list
        if not head.next.next:
            mid_next = head.next
            head.next = None
        else:
            mid_next = slow_ptr.next
            slow_ptr.next = None

        l1 = self.merge_sort(head)
        l2 = self.merge_sort(mid_next)
        head = self.merge(l1, l2)
        return head

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    # ll.append(11)
    # ll.append(9)
    # ll.append(8)
    # ll.append(7)
    # ll.append(2)
    # ll.append(2)
    # ll.append(2)


    result_head = ll.merge_sort(ll.head)
    while result_head:
        print(result_head.val, end=" ")
        result_head = result_head.next
    print()
