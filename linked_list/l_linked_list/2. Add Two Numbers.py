# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode(-1)
        carry = 0
        
        while l1 and l2:
            summ = l1.val + l2.val + carry 
            carry = summ // 10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            summ = l1.val + carry
            carry = summ // 10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            l1 = l1.next
        while l2:
            summ = l2.val + carry
            carry = summ // 10
            curr.next = ListNode(summ % 10)
            curr = curr.next
            l2 = l2.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
            
