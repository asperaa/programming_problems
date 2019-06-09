# class Node

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# class Function
class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while(fast_ptr.next is not None):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":

    ll = LinkedList()
    ll.push(2)
    ll.push(8)
    ll.push(10)
    ll.push(12)
    ll.push(13)
    ll.push(14)
    ll.push(15)

    ll.print_list()
    print(ll.middle())