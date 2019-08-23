"""Random pointer linked list deep copy in constant space"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def deep_clone(self, head):
        if not head:
            return head
        curr_node = head
        next_node = None
        
        # make the 1->1->2->2->3->3->4->4 pattern
        while curr_node:
            new_node = ListNode(curr_node.val)
            # check if random is None by storing -- comment 1
            new_node.random = curr_node.random
            next_node = curr_node.next
            curr_node.next = new_node
            new_node.next = next_node
            curr_node = next_node
        # copy the random pointer
        curr_node = head
        while curr_node:
            if curr_node.next.random: # here we use the comment 1
                curr_node.next.random = curr_node.random.next
            curr_node = curr_node.next.next
        
        new_head = head.next
        # separate original and clone ll
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return new_head




if __name__ == "__main__":
    ll = LinkedList()
    ll.append(-1)
    ll.append(8)
    ll.append(7)
    ll.append(-3)
    ll.append(4)
    ll.head.random = ll.head.next.next.next.next
    ll.head.next.random = ll.head.next.next.next
    ll.head.next.next.next.random = ll.head
    # ll.head.random = ll.head.next.next
    # ll.head.next.random = ll.head.next.next.next
    print(ll.head.next.next.next.random.val)
    result_head = ll.deep_clone(ll.head)
    temp = result_head
    while temp:
        if temp.random:
            print(temp.val, temp.random.val)
        else:
            print(temp.val, " ")
        temp = temp.next
    print()

    # print(result_head.random.val)
    # print(result_head.val)
    # print(result_head.next.next.next.next.random.val)
