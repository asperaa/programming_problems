"""Add the two numbers who are stroed in reverse order"""
# Linked List Node data structure
class Node:
    # Initialise the linked list with the data
    def __init__(self, val):
        self.val = val
        self.next = None
# Linked list class
class LinkedList:
    # Initialise the head of the linked list
    def __init__(self):
        self.head = None
    # add a node to the end of the linked list
    def append(self, val):
        # create a node
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
        return
    # print a linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.val
        print()
    # sum of digits function
def sum_of_digits(l1, l2):
    temp1 = l1.head
    temp2 = l2.head
    carry = 0
    result_list = None
    head_result = None
    while(temp1 and temp2):
        num_sum = temp1.val + temp2.val + carry
        last_digit = num_sum%10
        carry = num_sum//10
        if not result_list:
            result_list = Node(last_digit)
            head_result = result_list
        else:
            result_list.next = Node(last_digit)
            result_list = result_list.next
        temp1 = temp1.next
        temp2 = temp2.next
    while(temp1):
        num_sum = temp1.val + carry
        last_digit = num_sum%10
        carry = num_sum/10
        result_list.next = Node(last_digit)
        result_list = result_list.next
        temp1 = temp1.next
    while(temp2):
        num_sum = temp2.val + carry
        last_digit = num_sum%10
        carry = num_sum//10
        result_list.next = Node(last_digit)
        result_list = result_list.next
        temp2 = temp2.next
    if carry:
        result_list.next = Node(carry)
    return head_result

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    l1.append(1)


    l2.append(9)
    l2.append(9)
    # l2.append(4)
    
    result = sum_of_digits(l1, l2)
    while(result):
        print(result.val, end=" ")
        result = result.next
    print()

        

