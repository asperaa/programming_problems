class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None 
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if not self.head:
            return -1
        mover = self.head
        while index>0 and mover:
            mover = mover.next
            index -= 1
            
        if not mover or index < 0:
            return -1
        return mover.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        mover = self.head
        while mover.next:
            mover = mover.next
        mover.next = new_node
        return
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if index < 1:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while index > 1 and temp:
            temp = temp.next
            index -= 1
        if not temp:
            return
        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node
        return
            
            
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if not self.head:
            return

        temp = self.head
        if index == 0:
            self.head = self.head.next
            return
        while index - 1 and temp.next:
            temp = temp.next
            index -= 1
        if index != 1:
            return
        if not temp.next:
            return
        next_node = temp.next.next
        temp.next = next_node
        return
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = MyLinkedList()
    # ll.addAtHead(1)
    # ll.addAtTail(3)
    ll.addAtIndex(-1, 0)
    print(ll.get(0))
    # ll.deleteAtIndex(0)
    ll.print_list()
