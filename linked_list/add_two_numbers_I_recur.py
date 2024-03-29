"""Add two numbers as linked list I """
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
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
            print(temp.data, end=" ")
            temp = temp.next
        print()
        return
    # can solve using recusion.
    # Go till the end for longer one. Keep adding Zero valued node for shorter one
    #Keep adding nodes if there is a carry left
    def add_two(self, l1, l2, c=0):
        val = l1.data + l2.data + c

        c = val//10
        ret_node = Node(val%10)

        if (l1.next != None or l2.next != None or c != 0):
            # add zero node if l1 is short
            if l1.next == None:
                l1.next = Node(0)

            # add zero node if l2 is short   
            if l2.next == None:
                l2.next = Node(0)
            
            # assign the next val using recusion
            ret_node.next = self.add_two(l1.next, l2.next, c)
        
        # return call is important
        return ret_node

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(2)
    ll.append(4)
    ll.append(7)
    ll.print_list()
    
    ll_two = LinkedList()
    ll_two.append(5)
    ll_two.append(6)
    ll_two.append(7)
    ll_two.print_list()

    ll_result = ll.add_two(ll.head, ll_two.head)
    temp = ll_result
    # print(temp.data)
    print(temp.next.data)
    while(temp):
        print(temp.data, end=" ")
        temp = temp.next


