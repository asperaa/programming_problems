"""Rotate the linked list counter clockwise -- Two passes allowed"""
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
    
    def get_length(self):
        length = 0
        mover = self.head
        while mover:
            mover = mover.next
            length += 1
        return length

    def rotate(self, k):
        # if zero or single nodes are there in linked list
        if not self.head or not self.head.next:
            return self.head

        length = self.get_length()
        if k >= length:
            partial_path = length - (k%length)
        else:
            partial_path = length - k
        
        if partial_path == length:
            return self.head

        new_head = self.head
        prev = self.head
        original_head = self.head
        mover = self.head
        
        while partial_path:
            prev = mover
            mover = mover.next
            partial_path -= 1
        new_head = mover
        prev.next = None

        while mover.next:
            mover = mover.next
        mover.next = original_head

        self.head = new_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.print_list()
    
    ll.rotate(3)
    ll.print_list()
