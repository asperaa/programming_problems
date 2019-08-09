"""Find the cyclic node in the linked list"""
# Node class for linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#LinkedList class
class LinkedList:
    # initialise the head of the linked list
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        return

    def find_node(self):

        # find the length of the cycle
        slow_ptr = self.head
        fast_ptr = self.head
        count_length = 0
        while(slow_ptr and fast_ptr and fast_ptr.next):
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            # when the fast and slow ptr meet in the loop
            # hold the fast_ptr and move the slow_ptr to meet the 
            # fast ptr again. Maintain a counter to counte num of nodes.
            if slow_ptr == fast_ptr:
                count_length += 1
                slow_ptr = slow_ptr.next
                while(slow_ptr != fast_ptr):
                    slow_ptr = slow_ptr.next
                    count_length += 1
                break
        if count_length == 0:
            return None
        # Actually find the starting node of the loop
        first_mover = self.head
        second_mover = self.head
        while(count_length):
            first_mover = first_mover.next
            count_length = count_length - 1

        while(first_mover != second_mover):
            first_mover = first_mover.next
            second_mover = second_mover.next
        
        return second_mover
        
            
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)

    ll.head.next.next.next.next.next.next.next = ll.head.next.next

    result = ll.find_node()
    if result:
        print(result.val)