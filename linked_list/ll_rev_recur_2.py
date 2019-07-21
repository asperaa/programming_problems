"""Reverse a linked list using recusion (practice 2)"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        return
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        temp = self.reverse(head.next)
        head.next.next = head
        head.next = None
        self.head = temp
        return temp

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.print_list()
    ll.reverse(ll.head)
    ll.print_list()