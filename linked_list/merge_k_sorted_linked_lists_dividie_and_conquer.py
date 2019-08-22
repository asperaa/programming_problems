"""Merge K sorted linked lists using divide and conquer in O(1) space"""
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


    def merge_2_lists(self, l1, l2):
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

    def merge_k_lists(self, lists):
        if not lists:
            return None
        start = 0
        end = len(lists) - 1
        print(end)
        while start != end or end != 0:
            if start >= end:
                start = 0
            else:
                lists[start] = self.merge_2_lists(lists[start], lists[end])
                start += 1
                end -= 1

        return lists[0]

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()

    l1.append(1)
    l1.append(4)
    l1.append(7)
    l2.append(3)
    l2.append(9)
    l2.append(10)
    l3.append(19)

    lists = [l1.head, l2.head, l3.head]

    result_head = l1.merge_k_lists(lists)
    while result_head:
        print(result_head.val, end=" ")
        result_head = result_head.next
    print()


