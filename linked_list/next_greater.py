"""Output an array with each element indicating the next greater 
   elment in the ll"""
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

    def next_greater(self):
        if not self.head:
            return
        mover = self.head
        ans = []
        stack = []
        pos = -1
        while mover:
            pos += 1
            while stack and stack[-1][1] < mover.val:
                idx, _ = stack.pop()
                ans[idx] = mover.val
            ans.append(0)
            stack.append([pos, mover.val])
            mover = mover.next
        return ans
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(9)
    ll.append(7)
    ll.append(6)
    ll.append(7)
    ll.append(6)
    ll.append(9)

    print(ll.next_greater())