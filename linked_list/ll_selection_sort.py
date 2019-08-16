"""Selection sort in a linked list"""
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

    def swap(self, prev_i, prev_min):
        # if self.head == prev_i:
        #     next_min = prev_min.next
        #     head_next = self.head.next
        #     self.head.next = next_min.next
        #     next_min.next = head_next
        #     prev_min.next = self.head
        #     self.head = next_min
        #     return
        print("SWAP", prev_i.val, prev_min.val)
        next_i = prev_i.next
        next_min = prev_min.next
        min_next_next = next_i.next
        next_i.next = next_min.next
        next_min.next = min_next_next
        prev_i.next = next_min
        prev_min.next = next_i
        
        return 
    
    def selection_sort(self):
        temp = self.head
        prev_i = self.head
        prev_min = self.head
        flag = 0
        while temp:
            curr = temp
            prev_i = temp
            prev_min = temp
            while curr and curr.next:
                # print(curr.val, end=" ")
                if curr.next.val < prev_min.next.val:
                    prev_min = curr
                    flag = 1
                #     print("HERE")
                    break
                curr = curr.next
            if flag == 1:
                temp = self.head
                while temp:
                    print(temp.val, end=" ")
                    temp = temp.next
                print()
                break


            self.swap(prev_i, prev_min)
            temp = temp.next

if __name__ == "__main__":        
    ll = LinkedList()
    ll.append(10)
    ll.append(8)
    ll.append(11)
    ll.append(3)
    ll.append(6)

    ll.print_list()
    ll.swap(ll.head, ll.head.next)
    ll.print_list()
    # ll.selection_sort()
    # ll.print_list()
