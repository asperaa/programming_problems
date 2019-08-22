"""Flatten a linked list"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.down = None

class LinkedList:
    def __init__(self):
        self.real_head = None

    def down_append(self, head, val):
        new_node = ListNode(val)
        if not head:
            self.real_head = new_node
            head = new_node
            return
        temp = head
        while temp.down:
            temp = temp.down
        temp.down = new_node
        return
    
    def right_append(self, head, val):
        new_node = ListNode(val)
        if not head:
            self.real_head = new_node
            head = new_node
            return
        temp = head
        while temp.right:
            temp = temp.right

        temp.right = new_node
        return
    
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val <= l2.val:
            result = l1
            result.down = self.merge(l1.down, l2)
        else:
            result = l2
            result.down = self.merge(l1, l2.down)
        return result
    
    def flatten(self, root):
        if root == None or root.right == None:
            return root
        result = self.merge(root, self.flatten(root.right))
        return result

if __name__ == "__main__":
    ll = LinkedList()
    ll.down_append(ll.real_head, 1)
    ll.down_append(ll.real_head, 3)
    ll.down_append(ll.real_head, 8)
    ll.down_append(ll.real_head, 13)

    ll.right_append(ll.real_head, 2)
    ll.right_append(ll.real_head, 4)
    ll.right_append(ll.real_head, 5)
    
    ll.down_append(ll.real_head.right, 6)
    ll.down_append(ll.real_head.right, 11)
    ll.down_append(ll.real_head.right, 15)
    ll.down_append(ll.real_head.right, 20)

    ll.down_append(ll.real_head.right.right, 9)
    ll.down_append(ll.real_head.right.right, 10)
    ll.down_append(ll.real_head.right.right.right, 7)
    ll.down_append(ll.real_head.right.right.right, 12)
    ll.down_append(ll.real_head.right.right.right, 14)

    result = ll.flatten(ll.real_head)
    while result:
        print(result.val, end=" ")
        result = result.down
    print()
    
