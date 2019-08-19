"""Reverse a linked list at m and n positions in one pass"""
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
    
    def reverse(self, n, m):
        prev_node = None
        curr_node = self.head
        next_node = None
        start_node = None
        end_node = None
        prev_start = None
        temp = self.head
        counter = 0
        
        while m>=0:
            counter += 1
            if counter == n:
                start_node = prev_start
                curr_node = temp
                while m>0:
                    next_node = curr_node.next
                    curr_node.next = prev_node
                    prev_node = curr_node
                    curr_node = next_node
                    m -= 1
                end_node = curr_node
            # keep track of the previous value
            prev_start = temp
            if temp:
                temp = temp.next
            m -= 1
        # case of head node
        if n == 1:
            self.head.next = end_node
            self.head = prev_node
            return self.head

        rev_head = start_node.next
        start_node.next = prev_node
        rev_head.next = end_node
        
        return self.head


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
    ll.reverse(1, 7)
    ll.print_list()
