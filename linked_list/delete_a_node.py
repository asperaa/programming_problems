"""Delete node the node in a linked list without the head given"""
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
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def delete(self, node):
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(4)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)

    ll.print_list()
    ll.delete(ll.head.next)
    ll.print_list()