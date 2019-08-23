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
        original_head = head
        store_node = dict()
        
        while head:
            new_node = ListNode(head.val)
            store_node[head] = new_node
            head = head.next
        
        head = original_head
        clone_head = None
        while head:
            clone_head = store_node[head]
            if not head.next:
                clone_head.next = None
            else:
                clone_head.next = store_node[head.next]
            if not head.random:
                clone_head.random = None
            else:
                clone_head.random = store_node[head.random]
            head = head.next
            
        return store_node[original_head] 

                               
        
            

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
