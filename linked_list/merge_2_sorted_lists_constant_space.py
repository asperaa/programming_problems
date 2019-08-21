"""Merge 2 sorted linked lists in linear time and constant space"""
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
    
def merge_2_lists(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l2.next
        point = point.next
    
    if l1:
        point.next = l1
    else:
        point.next = l2

    return head.next

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append(1)
    l1.append(6)
    l1.append(7)
    l2.append(3)
    l2.append(4)
    l2.append(8)
    result_list = merge_2_lists(l1.head, l2.head)
    while result_list:
        print(result_list.val, end=" ")
        result_list = result_list.next
    print()



            