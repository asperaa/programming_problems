# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def rev_k(pivot_head, k):
        
        curr_node = pivot_head
        prev_node = None
        next_node = None
        
        while k:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            k -= 1
        
        new_head = prev_node
        return new_head, pivot_head, next_node
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.get_length(head)
        
        if not head or not head.next or k > length:
            return head
        
        counter = k
        curr_node = head
        prev_node = None
        next_node = None
        
        while counter:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            counter -= 1
        pivot_head = head
        head = prev_node
        
        num_loops = length // k
        
        while num_loops:
            pivot_head.next, pivot_head, next_node = self.rev_k(next_node, k)
            num_loops -= 1
        if next_node:
            pivot_head.next = next_node
        
        return head