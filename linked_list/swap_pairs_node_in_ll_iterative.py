"""Swap pairs of the nodes in linked list iteratively"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        return

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def swap_pair(self, head):
        if not head or not head.next:
            return head

        curr = head.next.next
        prev = head
        new_head = head.next
        head.next.next = head

        while curr and curr.next:
            prev.next = curr.next
            prev = curr
            next_node = curr.next.next
            curr.next.next = curr
            curr = next_node
        prev.next = curr

        return new_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(5)
    ll.add_front(4)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)

    ll.print_list()
    head = ll.swap_pair(ll.head)

    while head:
        print(head.val, end=" ")
        head = head.next
    print()


