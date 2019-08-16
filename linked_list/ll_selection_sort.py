"""Selection sort in a linked list (TODO: Rectify this one)"""
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

    def swap(self, node_a, node_b):
        prev_a = self.head
        prev_b = self.head
        print("Pairs:", node_a.val, node_b.val)
        while prev_a and prev_a.next != node_a:
            prev_a = prev_a.next
        
        while prev_b and prev_b.next != node_b:
            prev_b = prev_b.next
        
        # one of the node is head node
        if self.head == node_a:
            # nodes are adjacnet
            if node_a.next == node_b:
               node_a.next = node_b.next
               node_b.next = node_a
               self.head = node_b
            else:     
                next_b = node_b.next
                node_b.next = self.head.next
                node_a.next = next_b
                prev_b.next = self.head
                self.head = node_b
        else:
            # nodes are adjacent
            if node_a.next == node_b:
                node_a.next = node_b.next
                node_b.next = node_a
                prev_a.next = node_b          
            else:
                next_a = node_a.next
                next_b = node_b.next
                node_a.next = next_b
                node_b.next = next_a
                prev_a.next = node_b
                prev_b.next = node_a
        
        return
    
    def selection_sort(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            curr = temp
            i = temp
            minn = temp
            while curr:
                if curr.val < minn.val:
                    minn = curr
                curr = curr.next
            print(minn.val, count)
            print(i.val, minn.val)
            self.swap(i, minn)
            temp = temp.next
        print(count)

if __name__ == "__main__":        
    ll = LinkedList()
    ll.append(2)
    ll.append(8)
    ll.append(11)
    ll.append(3)
    ll.append(6)

    ll.print_list()
    # ll.swap(ll.head.next, ll.head.next.next.next)
    ll.print_list()
    ll.selection_sort()
    ll.print_list()
