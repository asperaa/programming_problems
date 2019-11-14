"""Add two numbers represented by a linked list when
   most significant digit is is present in first node"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def reverse(self, head):
        prev_node = None
        curr_node = head
        next_node = head
        
        while(curr_node):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head
                   
        
    # Can use same method as the add two numbers I(reverse numbers)
    # Caveat: Reverse both the lls. Do Add Num I stuff. 
    # Reverse the result.
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rev_l1 = self.reverse(l1)
        rev_l2 = self.reverse(l2)
        carry = 0
        sum_digit = 0
        result_sum = 0
        result_ll = None
        head_result = None
        while(rev_l1 and rev_l2):
            sum_digit = rev_l1.val + rev_l2.val + carry
            result_sum = sum_digit%10
            carry = sum_digit//10
            
            new_node = ListNode(result_sum)
            if not result_ll:
                result_ll = new_node
                head_result = result_ll
            else:
                result_ll.next = new_node
                result_ll = result_ll.next
            rev_l1 = rev_l1.next
            rev_l2 = rev_l2.next
        
        while rev_l1:
            sum_digit = rev_l1.val + carry
            result_sum = sum_digit%10
            carry = sum_digit//10
            
            new_node = ListNode(result_sum)
            result_ll.next = new_node
            result_ll = result_ll.next
            rev_l1 = rev_l1.next
            
        while rev_l2:
            sum_digit = rev_l2.val + carry
            result_sum = sum_digit%10
            carry = sum_digit//10
            
            new_node = ListNode(result_sum)
            result_ll.next = new_node
            result_ll = result_ll.next
            rev_l2 = rev_l2.next
        
        if carry:
            new_node = ListNode(carry)
            result_ll.next = new_node
            result_ll = result_ll.next
            
        result_ll = self.reverse(head_result)
        return result_ll
            
            
            
            
            
        
        
        