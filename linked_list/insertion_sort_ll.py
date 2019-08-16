"""Sort the linked list using insertion sort. Can use O(n) space"""
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
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
    def sorted_insert(self, head, new_node):
        if head.val > new_node.val:
            new_node.next = head
            head = new_node
            return head

        temp = head
        while temp.next and new_node.val >= temp.next.val:
            temp = temp.next

        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node
        return head


    def insertion_sort(self, head):
        curr = self.head
        while curr:
            next_node = curr.next
            head = self.sorted_insert(head, curr)
            curr = next_node
            print("YES")
        return head
        
        return head
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(9)
    ll.append(11)
    ll.append(10)
    ll.append(12)
    ll.append(10)
    # ll.append(7)
    # ll.append(6)
    # ll.append(5)
    ll.print_list()
    head = ll.insertion_sort(ll.head)
    # ll.print_list()
    while head:
        print(head.val, end=" ")
        head = head.next
    print()



        

