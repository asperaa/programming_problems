# Node class
class Node:

    # function to start a node and fill data
    def __init__(self, data):
        self.data = data # fill the data
        self.next = None # point the next of linked list to null

# LinkedList class
class LinkedList:

    # function to initialise a linked_List
    def __init__(self):
        self.head = None
    
    # function to add new nodes in the srart of ll
    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # function to count the node (iterative)
    def get_count(self):
        # intialise the counter of nodes and temp node pointer
        ctr = 0
        temp = self.head

        while(temp is not None):
            ctr = ctr + 1
            temp = temp.next
        
        return ctr
    
    # helper function that counts number of nodes recusivley given the head of a node
    def get_count_rec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.get_count_rec(node.next)

    # wrapper for get_count_rec() function
    def get_count_wrap(self):
        return self.get_count_rec(self.head)


if __name__ == '__main__':
    
    ll = LinkedList()
    ll.push(8)
    ll.push(10)
    ll.push(10)
    ll.push(80)

    print("Rec. count",ll.get_count_wrap())
    print("Iter. count", ll.get_count())