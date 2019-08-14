"""Rotate the linked list using single pass"""
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
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def rotate(self, k):
        if not self.head or not self.head.next:
            return self.head
        
        first_pointer = self.head
        second_pointer = self.head
        length = 0
        counter = k
        while counter:
            if not second_pointer.next:
                length += 1
                second_pointer = self.head
                counter  = k%length
                length = 0
                continue
            second_pointer = second_pointer.next
            counter -= 1
            length += 1
        if first_pointer == second_pointer:
            return self.head

        while second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        new_head = first_pointer.next
        first_pointer.next = None
        second_pointer.next = self.head
        self.head = new_head
        return

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.print_list()

    ll.rotate(6)
    ll.print_list()

            

        
            