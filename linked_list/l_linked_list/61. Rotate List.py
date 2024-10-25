# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def get_length(self, head):
        ll_length = 0
        temp = head
        while temp:
            temp = temp.next
            ll_length += 1
        return ll_length
    
    
    
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        ll_length = self.get_length(head)
        rotate_length = k % ll_length
        if rotate_length == 0:
            return head
        
        leftout_rotate_length = ll_length - rotate_length - 1
        
        temp = head
        while leftout_rotate_length:
            temp = temp.next
            leftout_rotate_length -= 1
        new_head = temp.next
        temp.next = None
        temp_new_head = new_head
        
        while temp_new_head.next:
            temp_new_head = temp_new_head.next
        temp_new_head.next = head
        return new_head