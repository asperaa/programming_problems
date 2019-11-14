"""Add two numbers represented by linked lists using a second method"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
        return
# function to get the length of the linked list
def get_length(ll):
    length = 0
    mover = ll
    while(mover):
        length += 1
        mover = mover.next
    return length

# function to to add leading zeroes to the shorter linked list
def add_leading_zeroes(num, ll):
    while(num):
        new_node = ListNode(0)
        new_node.next = ll
        ll = new_node
        num -= 1
    return ll


# Use recursion to reach the end of both ll simultaneously
# Keep the carry when you return something
def combine_ll(head_l1, head_l2):
    if not head_l1 and not head_l2:
        return (0, None)
    
    carry, new_node = combine_ll(head_l1.next, head_l2.next)
    sum_value = head_l1.val + head_l2.val + carry
    carry = sum_value//10
    curr_node = ListNode(sum_value%10)
    curr_node.next = new_node
    return (carry, curr_node)

# actually executes the combined linked list function and takes care of the last carry
def add_two_num(l1, l2):
    length_l1, length_l2 = get_length(l1), get_length(l2)
    if length_l1 > length_l2:
        l2 = add_leading_zeroes(length_l1 - length_l2, l2)
    else:
        l1 = add_leading_zeroes(length_l2 - length_l1, l1)
    carry, result_ll = combine_ll(l1, l2)
    
    if carry:
        new_node = ListNode(carry)
        new_node.next = result_ll
        result_ll = new_node
    return result_ll

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    l1.append(7)
    l1.append(2)
    l1.append(4)
    l1.append(3)

    l2.append(5)
    l2.append(6)
    l2.append(4)

    result_ll = add_two_num(l1.head, l2.head)
    while(result_ll):
        print(result_ll.val, end=" ")
        result_ll = result_ll.next
    print()
