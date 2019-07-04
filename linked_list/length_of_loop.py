"""Find the lenght of loop in linked list """
# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    
    # initialise the head of linked list
    def __init__(self):
        self.head = None
    # add a new node to the end of linked list
    def add_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    # print the linked list
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    # find the length of the loop
    def loop_length(self):

        if self.head is None:
            return
        
        hash_set = set()
        temp = self.head
        count = 0
        while(temp):
            if temp in hash_set:
                break
            else:
                hash_set.add(temp)
            count += 1
            temp = temp.next
        return count

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_front(7)
    ll.add_front(6)
    ll.add_front(5)
    ll.add_front(5)
    ll.add_front(4)
    ll.add_front(3)
    ll.add_front(2)
    ll.add_front(1)
    ll.print_list()
    ll.head.next.next.next.next.next.next.next.next = ll.head
    print(ll.loop_length())
