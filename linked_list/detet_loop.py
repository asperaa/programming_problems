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
    
    def detect_loop(self):
        # initialise a set to store the node addresses
        s = set()
        temp = self.head

        while(temp):
            # check if the node is already visited
            if temp in s:
                print("loop detected")
                return True
            # add the node to the hash map
            s.add(temp) 

            # check for next node   
            temp = temp.next
        
        return False

    def detect_loop_floyd(self):

        slow_ptr = self.head
        fast_ptr = self.head

        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                print("Flyod loop detected.")
                return True
        return False

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":

    ll = LinkedList()
    ll.push(8)
    ll.push(9)
    ll.push(10)
    ll.push(13)
    ll.push(15)
    ll.push(17)
    
    ll.print_list()
    print(ll.detect_loop())
    ll.head.next.next.next.next = ll.head
    # ll.print_list()
    print(ll.detect_loop())
    print(ll.detect_loop_floyd())

