import gc

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def append(self, data):
        
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while(temp.next):
            temp = temp.next
        
        temp.next = new_node
    
    def del_dup(self):

        if self.head is None:
            return
        
        curr = self.head
        
        while(curr.next):
            if curr.data == curr.next.data:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
            else:
                curr = curr.next
        gc.collect()

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.append(5)
    ll.append(5)

    ll.print_list()
    
    ll.del_dup()

    ll.print_list()