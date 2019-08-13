"""Swap apirs of node in ll"""
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
        while mover.next:
            mover = mover.next
        mover.next = new_node
        return

    def print_list(self):
        temp = self.head
        while temp:
            print (temp.val, end=" ")
            temp = temp.next
        print()
    
    def swap_pairs(self, head):
        if not head or not head.next:
            return head
         # store the new_node
        new_head = head.next
        # store the reamining list 
        remaining_list = head.next.next
        # change the next pointer of the second node to be the first node
        head.next.next = head

        # recursive call to swap pairs of the remaining list
        head.next = self.swap_pairs(remaining_list)

        # return the new head
        return new_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.print_list()
    head = ll.swap_pairs(ll.head)
    while head:
        print(head.val, end=" ")
        head = head.next
    print()