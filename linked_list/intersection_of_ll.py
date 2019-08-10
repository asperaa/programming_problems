"""FInd the intersection of two linked lists"""
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
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node
        return
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()
    
def intersection(l1, l2):
    l1_length = 0
    l2_length = 0
    l1_mover = l1.head
    l2_mover = l2.head
    while(l1_mover):
        l1_length += 1
        l1_mover = l1_mover.next
    
    while(l2_mover):
        l2_length += 1
        l2_mover = l2_mover.next
    l1_mover = l1.head
    l2_mover = l2.head
    if l1_length > l2_length:
        balance_length = l1_length - l2_length

        while(balance_length):
            l1_mover = l1_mover.next
            balance_length -= 1
        
        while(l1_mover != l2_mover):
            l1_mover = l1_mover.next
            l2_mover = l2_mover.next
        
        return l1_mover
    else:
        balance_length = l2_length - l1_length
        
        while(balance_length):
            balance_length -= 1
            l2_mover = l2_mover.next

        while(l1_mover != l2_mover):
            l1_mover = l1_mover.next
            l2_mover = l2_mover.next
        
        return l1_mover
    return None 


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.append(6)

    l2 = LinkedList()
    l2.append(7)
    l2.append(8)
    l2.append(9)

    l2.head.next.next.next = l1.head.next.next

    intersection_node = intersection(l1, l2)

    print(intersection_node.val)

    