# Node class
class Node:
    
    # function to initialsie the node
    def __init__(self, data):
        self.data = data # fill the data
        self.next = None # poit the next to a null

# LinkedList class
class LinkedList:

    # function to initialise a node with head pointing to null
    def __init__(self):
        self.head = None
    
    # function to point to add a new_node to front of ll
    def push(self, data):
        new_node = Node(data) # initialise a node and fill the data
        new_node.next = self.head # point the next of node to head of ll
        self.head = new_node # point the head of node to this new node
    
    # function to search for a key (iteratively)
    def search_itr(self, key):
        # initialise the temp pointer
        temp = self.head
        while(temp is not None):
            if temp.data == key:
                return True
            temp = temp.next
        
        return False
    
    # function to check for a key (recursively)

    def search_rec(self, node, key):
        
        # Base case
        if not node:
            return False
        # if the key is present in the current node, return true
        if node.data == key:
            return True
        
        return self.search_rec(node.next, key)


if __name__ == "__main__":
    
    ll = LinkedList()
    ll.push(1)
    ll.push(3)
    ll.push(8)
    ll.push(12)
    print(ll.search_rec(ll.head, 9))
    print(ll.search_itr(11))

   