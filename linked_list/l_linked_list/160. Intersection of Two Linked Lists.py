# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, l1, l2):
        headA = l1
        headB = l2
        
        if not headA or not headB:
            return None
        
        while l1 != l2:
            if l1:
                l1 = l2.next
            else:
                l1 = headB
            if l2:
                l2 = l2.next
            else:
                l2 = headA
        return l1
        
