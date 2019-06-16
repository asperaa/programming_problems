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
    
    def reverse(self):

        if self.head is None:
            print("Empty ll")
            return
        
        # initialise the prev_node and current node as None and head of ll
        prev_node = None
        curr_node = self.head

        while(curr_node is not None):
            next_node = curr_node.next # save the next of curr_node in a next_node var
            curr_node.next = prev_node # set the next of curr_node as prev_node
            prev_node = curr_node      # set the prev_node as curr_node
            curr_node = next_node      # set the curr_node as the next node that you saved earlier
            
        self.head = prev_node          # set the head of ll as the last node
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":

    ll = LinkedList()
    ll.push(8)
    ll.push(7)
    ll.push(4)
    ll.push(90)
    ll.push(10)

    ll.print_list()
    ll.reverse()
    ll.print_list()
