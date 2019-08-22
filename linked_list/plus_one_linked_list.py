"""Add one to a linked list when eac hnode denoates a digit of the number"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        return
    
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
    
    def reverse(self):
        prev_node = None
        curr_node = self.head
        next_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        return self.head


    def plus_one(self):
        rev_head = self.reverse()
        temp = rev_head
        carry = 1
        while temp:
            summ = temp.val + carry
            carry = summ//10
            actual_val = summ%10
            temp.val = actual_val
            temp = temp.next
            if carry == 0:
                break
        new_head = self.reverse()
        if carry:
            new_node = ListNode(1)
            new_node.next = self.head
            self.head = new_node
        return self.head
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(9)
    ll.append(9)
    ll.append(9)

    ll.plus_one()
    ll.print_list()


