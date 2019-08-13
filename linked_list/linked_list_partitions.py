"""Partition the linked list in K almost equal parts"""
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
        while(mover.next):
            mover = mover.next
        mover.next = new_node
        return
    
    def get_length(self):
        length = 0
        mover = self.head
        while(mover):
            length += 1
            mover = mover.next
        return length

    def partition(self, k):
        ans = [None]*k
        curr = self.head
        length = self.get_length()

        for i in range(k):
            num_elements = length//k + (1 if i < length%k else 0)
            
            for j in range(num_elements):
                if j == 0:
                    ans[i] = curr
                if j == num_elements - 1:
                    temp = curr.next
                    curr.next = None
                    curr = temp
                else:
                    curr = curr.next
        return ans  

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    print(ll.partition(3))


            