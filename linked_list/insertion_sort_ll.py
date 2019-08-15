"""Sort the linked list using insertion sort. Can use O(n) space"""
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
    
    def sorted_insert(self, new_node):
        if not self.head or self.head.val > new_node.val:
            new_node.next = self.head
            self.head = new_node
        temp = self.head
        while temp.next and new_node.val >= temp.next.val:
            temp = temp.next
        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node


    def insertion_sort(self):
        curr = self.head
        while curr:
            next_node = curr.next
            self.sorted_insert(curr)
            curr = next_node
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(10)
    ll.append(5)
    ll.print_list()
    ll.insertion_sort()
    ll.print_list()



        

