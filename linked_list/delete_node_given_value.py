"""Delete a node(s) given the value to be deleted"""
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
    
    def delete_nodes(self, val):
        if not self.head:
            return
        prev_node = self.head
        curr_node = self.head.next

        while(curr_node):
            if curr_node.val == val:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
                continue
            prev_node = curr_node
            curr_node = curr_node.next
        
        if self.head.val == val:
            self.head = self.head.next
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(6)
    ll.add_front(5)
    ll.add_front(4)
    ll.add_front(6)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)
    
    ll.print_list()
    ll.delete_nodes(1)
    ll.print_list()
