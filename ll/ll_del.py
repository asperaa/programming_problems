# class for a Node
class Node:

    # function to initialise the node
    def __init__(self, data):
        self.data = data  # fill the node with data
        self.next = None  # point the next of node to null

# class for a linked list
class LinkedList:

    # function to initialise a ll
    def __init__(self):
        self.head = None
    
    # function to add a node in the beginning of the linked list
    def push(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # function to add a node in the begging of the linked list
    def delete(self, key):
        
        # initialise the curr_node to search for the key in ll
        curr_node = self.head

        # check if the head of ll contains key
        if curr_node is not None:
            if curr_node.data == key:
                self.head = curr_node.next
                curr_node = None
                return

        # search for the key in the ll
        while(curr_node.data is not key and curr_node is not None):
            prev_node = curr_node
            curr_node = curr_node.next
        
        # check whether the key exist or not
        if curr_node is None:
            print("key does not exist")
            return
        
        # if the key does exist, then point the next of prev_node to next of new_node
        prev_node.next = curr_node.next

        curr_node = None
        
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    
    ll = LinkedList()
    ll.push(4)
    ll.push(5)
    ll.push(10)
    ll.push(90)

    ll.print_list()

    ll.delete(5)
    ll.print_list()
    ll.delete(4)
    ll.print_list()