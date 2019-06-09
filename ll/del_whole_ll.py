# Node class
class Node:

    # function to initialise a node
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class    
class LinkedList:
    
    # function to initialise the linked list
    def __init__(self):
        self.head = None
    
    # function to push new data to the ll
    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def deleteList(self):

        # initialise a temp pointer
        temp = self.head

        while(temp is not None):
            next_node = temp.next # save the next pointer
            del temp.data         # delete the current pointer
            temp = next_node      # move to the next node

    def print_list(self):
        temp = self.head # initialise the temp pointer
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":

    ll = LinkedList()
    ll.push(8)
    ll.push(90)
    ll.push(20)
    ll.print_list()

    print("Start delete process")
    ll.deleteList()
    print("Delete process over")