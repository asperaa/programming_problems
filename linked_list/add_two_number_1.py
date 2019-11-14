"""Add two numbers whose digits are represented by the node of ll. 
   Each number is present in a reversed order in ll nodes.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # temp nodes for each of the ll
        temp1 = l1
        temp2 = l2
        
        # initialize the carry node
        carry = 0
        
        # initialize the result_head and result _temp node
        result_list = None
        result_head = None
        
        # iterate over both the ll till one of them ends (differently sized ll)
        while(temp1 and temp2):
            # add the node values and carry (initial carry is zero)
            num_sum = temp1.val + temp2.val + carry
            
            # store the unit digit after sum
            last_digit = num_sum%10

            # store t he carry after sum
            carry = num_sum//10

            # start the head of the resultant list
            if not result_list:
                result_list = ListNode(last_digit)
                result_head = result_list
            # keep adding the summed nodes at the end of the resultant list
            else:
                result_list.next = ListNode(last_digit)
                result_list = result_list.next
            
            # move to the next nodes in both the ll
            temp1 = temp1.next
            temp2 = temp2.next
        
        # check whether first ll is longer ll.
        # if yes, then add the carry (if any) to this node ..
        while(temp1):
            num_sum = temp1.val + carry
            last_digit = num_sum%10
            carry = num_sum//10
            result_list.next = ListNode(last_digit)
            result_list = result_list.next
            temp1 = temp1.next
        
        # check whether second ll is longer node.
        # if yes, then add the carry (if any) to this node ..
        while(temp2):
            num_sum = temp2.val + carry
            last_digit = num_sum%10
            carry = num_sum//10
            result_list.next = ListNode(last_digit)
            result_list = result_list.next
            temp2 = temp2.next
        
        
        # check whether there is still a carry remaining.
        if carry:
            result_list.next = ListNode(carry) 
        return result_head