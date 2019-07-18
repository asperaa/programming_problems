""" do the pair-wise swap for the linked lists without swapping the data"""
# Node class
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data # fill the data in the data filed
        self.next = None # point the next of node to null

# linked list class
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    
    # add a new node to the front of linked list
    def add_front(self, data):
        # create a new node
        new_node = Node(data)
        # check if the new node of the class is empty
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    # print the list of print_list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    # pair wise swap helper function
    def pair_swap_helper(self, temp_head, k):
        current_node = temp_head
        next_node = None
        prev_node = None
        count = 0
        while(current_node and count < k):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            count += 1
        
        if next_node is not None:
            temp_head.next = self.pair_swap_helper(next_node, k)
        
        self.head = prev_node
        return prev_node
    
    # actual pair-wise swap function
    def pair_wise_swap(self):
        self.pair_swap_helper(self.head, 2)
if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(4)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)
    ll.print_list()

    ll.pair_wise_swap()

    ll.print_list()


        