# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        slow_ptr = head
        while slow_ptr and slow_ptr.next:
            if slow_ptr.next.val == val:
                slow_ptr.next = slow_ptr.next.next
                continue
            slow_ptr = slow_ptr.next
        if head and head.val == val:
            return head.next
        else:
            return head