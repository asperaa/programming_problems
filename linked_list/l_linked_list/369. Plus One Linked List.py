# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rev_ll(self, head):
        curr_node = head
        prev_node = None
        next_node = None
        
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head

    
    def plus_one_util(self, head):
        if not head:
            return None
        curr = prev = head
        while curr:
            curr_sum = curr.val + 1
            if curr_sum // 10 == 0:
                curr.val = curr_sum
                break
            curr.val = 0
            prev = curr
            curr = curr.next
            
        if curr_sum == 10:
            new_node = ListNode(1)
            prev.next = new_node
        return head
                
    
    def plusOne(self, head):
        reversed_head = self.rev_ll(head)
        reversed_head_plus_1 = self.plus_one_util(reversed_head)
        return self.rev_ll(reversed_head_plus_1)
