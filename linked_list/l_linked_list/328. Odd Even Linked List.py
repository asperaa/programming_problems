# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        odd_start = head
        even_start = head.next
        even_head = head.next
        prev_odd = None
        
        while odd_start and odd_start.next and even_start and even_start.next:
            prev_odd = odd_start
            odd_start.next = odd_start.next.next
            even_start.next = even_start.next.next
            odd_start = odd_start.next
            even_start = even_start.next
        
        if odd_start:
            odd_start.next = even_head
        else:
            prev_odd.next = even_head
        return head
