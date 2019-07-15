""" Reverse a group of linked list """
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    # add a new node to the end of linked list
    def add_node(self, data):
        # create a new node
        new_node = Node(data)
        # check if the node is empty
        if self.head is None:
            self.head = new_node
            return
        # mover node
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
         
    def reverse_k_group(self, temp_head, k):
        
        current_node = temp_head
        next = None
        prev_node = None
        count = 0
        # break the loop on reaching the group limit
        # and on end of ll
        while(current_node is not None and count < k):
            next = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next
            count += 1
        # stop recursion on reaching the end of loop
        if next is not None:
            temp_head.next = self.reverse_k_group(next, k)
        
        # keep the head of the linked list updated
        self.head = prev_node
        # prev_node is the new_head of the input list
        return prev_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)
    ll.add_node(6)
    ll.add_node(7)
    ll.add_node(8)
    
    ll.print_list()

    ll.reverse_k_group(ll.head, 3)
    ll.print_list()






        


        
        