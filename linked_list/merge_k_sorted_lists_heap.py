"""Merge k sorted lists using in O(n*logk) time and 0(n) space"""
from queue import PriorityQueue
class use_only_first:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __lt__(self, other):
        return self._first < other._first


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
    
    def mergeKLists(self, lists):
        q = PriorityQueue()
        for head_node in lists:
            if head_node:
                q.put(use_only_first(head_node.val, head_node))
        
        head = point = ListNode(0)

        while not q.empty():
            object_node = q.get()
            val = object_node._first
            node = object_node._second
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put(use_only_first(node.val, node))
             
        return head.next
    
if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()

    l1.append(1)
    l1.append(2)
    l1.append(3)
    l2.append(6)
    l2.append(17)
    l3.append(5)
    l3.append(70)
    l3.append(80)

    arr = [l1.head, l2.head, l3.head]

    result = l1.mergeKLists(arr)
    while result:
        print(result.val, end=" ")
        result = result.next
    print()



