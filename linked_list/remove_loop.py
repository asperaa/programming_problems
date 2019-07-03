"""Remove loop in the linked list """
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # initialise the head of linked list
    def __init__(self):
        self.head = None
    
    # add a new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
    
    # print the linked list
    def print_list(self):
        temp = self.head
        counter = 0
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
            counter += 1
            if counter == 40:
                break
        print()
    
    # remove the loop
    def remove_loop(self):
        # check if the linked list is empty
        if self.head is None:
            return
        
        mover = self.head
        loop_point = self.head

        hash_set = set() 
        while(mover.next):
            if mover.next in hash_set:
                loop_point = mover
                break
            else:
                hash_set.add(mover)
                mover = mover.next
        loop_point.next = None

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    
    ll.print_list()
    ll.head.next.next.next.next.next.next.next = ll.head.next
    ll.print_list()
    ll.remove_loop()
    ll.print_list()
        
            

