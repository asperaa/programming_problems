"""Clone a linked list when you have a random pointer and next pointer 
   Space complexity is O(n) """
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
    
    def random_clone(self, head):
        clone_head = point = ListNode(0)
        store_node = dict()

        while head:
            new_node = ListNode(head.val)
            store_node[new_node] = head
            point.next = new_node
            point = point.next
            head = head.next
        clone_head = clone_head.next

        clone_ptr = clone_head
        while clone_ptr:
            clone_ptr.random = store_node[clone_ptr].random
            clone_ptr = clone_ptr.next
        return clone_head
            

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    ll.head.random = ll.head.next.next
    ll.head.next.random = ll.head.next.next.next

    result_head = ll.random_clone(ll.head)
    # while result_head:
    #     print(result_head.val, end=" ")
    #     result_head = result_head.next
    # print()

    print(result_head.random.val)
    print(result_head.next.random.val)
