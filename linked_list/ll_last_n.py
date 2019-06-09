# Node class
class Node:

    def __init__(self, data):
        self.data = data 
        self.next = None

# LinkedList class
class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def last_n_node(self, n):

        ref_ptr = self.head
        main_ptr = self.head
        ctr = 0

        while(ctr is not n):
            ref_ptr = ref_ptr.next
            ctr = ctr + 1
        
        while(ref_ptr is not None):
            ref_ptr = ref_ptr.next
            main_ptr = main_ptr.next

        return main_ptr.data


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(9)

    print(ll.last_n_node(3))    
