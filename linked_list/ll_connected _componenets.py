"""Find the connected componenets in ll"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while mover.next:
            mover = mover.next
        mover.next = new_node
        return
    def find_connected_components(self, G):
        # All the elements in G are unique so
        # put the elements in a set for fast lookup
        setG = set(G)
        ans = 0
        mover = self.head
        # traverse the linked list and modify the connected component count
        # by 1 when you find the end of the connected component
        # End of the CC arrives when curr val of node is present in G 
        # and next val is not present in G. Take care of the edge case 
        # of the last node
        while mover:
            if mover.val in setG and (mover.next == None or mover.next.val not in setG):
                 ans += 1
            mover = mover.next
        return ans

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    G = [1, 2, 4]
    print(ll.find_connected_components(G))

