"""find the first common elment in two linked list 
   i.e find the first node of the first list which is
   also present in the second list

Approach 3: Two Pointers
Maintain two pointers pApA and pBpB initialized at the head of A and B, respectively. 

Then let them both traverse through the lists, one node at a time.

When pApA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); 
similarly when pBpB reaches the end of a list, redirect it the head of A.
If at any point pApA meets pBpB, then pApA/pBpB is the intersection node.
To see why the above trick would work, consider the following two lists: A = {1,3,5,7,9,11} 
and B = {2,4,9,11}, which are intersected at node '9'. Since B.length (=4) < A.length (=6), 
pBpB would reach the end of the merged list first, because pBpB traverses exactly 2 nodes less than pApA does. 
By redirecting pBpB to head A, and pApA to head B, we now ask pBpB to travel exactly 2 more nodes than pApA would. 
So in the second iteration, they are guaranteed to reach the intersection node at the same time.
If two lists have intersection, then their last nodes must be the same one. 
So when pApA/pBpB reaches the end of a list, record the last element of A/B respectively. 
If the two last elements are not the same one, then the two lists have no intersections.   
"""
# Node class
class Node:
    # initialise the node with data and next pointer
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list class
class LinkedList:
    # inilialise the head of the ll
    def __init__(self):
        self.head = None
    
    # add a new node to the end of the linked list
    def add_end(self, data):
        # create a new node
        new_node = Node(data)
        # check if the ll is empty
        if self.head is None:
            self.head = new_node
            return
        mover = self.head
        while(mover.next):
            mover = mover.next
        mover.next = new_node
    
    # function to find the first common element in linked list

    
    # function to print the list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

def find_common(l1, l2):
    s = set()
    mover = l2.head
    while(mover):
        s.add(mover.data)
        mover = mover.next
    mover = l1.head
    while(mover):
        if mover.data in s:
            return mover.data
    
    return

if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_end(10)
    l1.add_end(15)
    l1.add_end(4)
    l1.add_end(20)

    l2 = LinkedList()
    l2.add_end(8)
    l2.add_end(4)
    l2.add_end(12)
    l2.add_end(10)

    print(find_common(l1, l2))
