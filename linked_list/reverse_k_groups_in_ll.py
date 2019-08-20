"""Reverse K groups in linked list"""
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

    def rev_k(self, pivot_head, k):
        prev_node = None
        curr_node = pivot_head
        next_node = None

        while k:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            k -= 1
        new_head = prev_node
        next_node = curr_node
        return new_head, pivot_head, next_node
            

    
    def length(self, head):
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        return size
        

    def reverse(self, head, k):
        size = self.length(head)
        if not head or not head.next or k > size:
            return head
        prev_node = None
        curr_node = head
        next_node = None
        group_size = k
        
        while group_size:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            group_size -= 1
        
        next_node = curr_node
        pivot_node = head
        head = prev_node
        loop_times = size//k

        for _ in range(loop_times-1):
            pivot_node.next, pivot_node, next_node = self.rev_k(next_node, k)
        if next_node:
            pivot_node.next = next_node

        return head

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.print_list()
    head = ll.reverse(ll.head, 2)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


        
