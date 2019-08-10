"""Check whether the linked list has a palindrome or not"""
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

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def palindrome(self):
        # find the middle of the linked list
        prev_middle = self.head
        slow_ptr = self.head
        fast_ptr = self.head
        while(fast_ptr and fast_ptr.next):
            prev_middle = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        middle_node = slow_ptr
        # reverse the second half of the linked list
        prev_node = prev_middle
        curr_node = middle_node
        next_node = middle_node

        while(curr_node):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        last_node = prev_node
        first_node = self.head
        
        # traverse the linked list from both sides
        while(first_node != last_node):
            if first_node.val != last_node.val:
                return False
            if first_node.next == last_node:
                break
            first_node = first_node.next
            last_node = last_node.next
        return True

if __name__ == "__main__":
    ll = LinkedList()

    ll.append(0)
    ll.append(0)
    # ll.append(0)
    # ll.append(0)
    # ll.append(1)
    # ll.append(1)

    ll.print_list()
    print(ll.palindrome())
        
        