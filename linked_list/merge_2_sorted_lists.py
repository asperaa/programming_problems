"""Merge 2 sorted lists using O(n) space"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_front(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
def merge(l1, l2):

    temp1 = l1.head
    temp2 = l2.head
    result_list = None
    result_head = None

    while(temp1 and temp2):
        if temp1.val <= temp2.val:
            new_node = ListNode(temp1.val)
            temp1 = temp1.next
        else:
            new_node = ListNode(temp2.val)
            temp2 = temp2.next        
        if not result_list:
            result_list = new_node
            result_head = result_list
        else:
            result_list.next = new_node
            result_list = result_list.next
    if l1 and not l2:
        result_list = ListNode(temp1.data)
        result_head = result_list
        temp1 = temp1.next
    
    if l2 and not l1:
        result_list = ListNode(temp2.data)
        result_head = result_list
        temp2 = temp2.next
        
    while(temp1):
        result_list.next = ListNode(temp1.val)
        result_list = result_list.next
        temp1 = temp1.next
    
    while(temp2):
        result_list.next = ListNode(temp2.val)
        result_list = result_list.next
        temp2 = temp2.next

    return result_head

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l1.add_front(7)
    l1.add_front(5)
    l1.add_front(3)

    l2.add_front(6)
    l2.add_front(4)
    l2.add_front(2)

    result = merge(l1, l2)

    while(result):
        print(result.val, end=" ")
        result = result.next
    print()
