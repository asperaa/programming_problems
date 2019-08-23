"""Add a number to the linked list where each node denotes the digit recursively"""
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
    
    def plus_one_helper(self, head):
        if not head:
            return 1
        res = head.val + self.plus_one_helper(head.next)
        head.val = res % 10
        carry = res // 10
        return carry
    
    def plus_one(self, head):
        carry = self.plus_one_helper(head)

        if carry:
            new_node = ListNode(1)
            new_node.next = head
            head = new_node
        return head

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(9)
    ll.append(9)
    ll.append(9)
    ll.append(9)

    result = ll.plus_one(ll.head)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()    