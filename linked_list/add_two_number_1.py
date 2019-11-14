# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1 = l1
        temp2 = l2
        carry = 0
        result_list = None
        result_head = None
        while(temp1 and temp2):
            num_sum = temp1.val + temp2.val + carry
            last_digit = num_sum%10
            carry = num_sum//10
            if not result_list:
                result_list = ListNode(last_digit)
                result_head = result_list
            else:
                result_list.next = ListNode(last_digit)
                result_list = result_list.next
            temp1 = temp1.next
            temp2 = temp2.next
        while(temp1):
            num_sum = temp1.val + carry
            last_digit = num_sum%10
            carry = num_sum//10
            result_list.next = ListNode(last_digit)
            result_list = result_list.next
            temp1 = temp1.next
        while(temp2):
            num_sum = temp2.val + carry
            last_digit = num_sum%10
            carry = num_sum//10
            result_list.next = ListNode(last_digit)
            result_list = result_list.next
            temp2 = temp2.next
        if carry:
            result_list.next = ListNode(carry) 
        return result_head