"""Reverse a linked list practice"""
# class for the node of linked list
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    # function to add a new node at the end
    def append(self, data):
        # create a new node
        new_node = Node(data)
        # check if the ll is empty
        if not self.head:
            self.head = new_node
            return
        # pointer to reach the end of the node
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
    # function to reverse a ll
    def reverse(self):
        # check if the linked list is empty
        if not self.head:
            return
        curr_node = self.head
        next_node = None
        prev_node = None

        while(curr_node):
            # save the next_node to move forward in original ll
            next_node = curr_node.next
            # change the next pointer of curr_node to prev_node
            curr_node.next = prev_node
            # change the prev_node to the curr_node
            prev_node = curr_node
            # update the curr_node to next_node because we want to move forward
            curr_node = next_node
        
        # change the head of the ll to be the last node
        self.head = prev_node
        return
    # print the list
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

    ll.print_list()
    ll.reverse()
    ll.print_list()      
