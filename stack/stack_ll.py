import gc

# Node class for stack elements
class Node:

    # function to initialise the node
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class
class Stack:
    
    # function to initialise the stack with top
    # and capacity variables 
    def __init__(self, capacity):
        self.top = None
        self.capacity = capacity
        self.counter = 0
    
    # function to check for empty stack
    def is_empty(self):
        if self.top == None:
            print("Stack is empty.")
            return True
        return False
    
    # function to check the top element of stack
    def peek(self):
        if self.is_empty():
           return
        return self.top.data
    
    # function to add new element in the stack
    def push(self, data):

        # check if the stack is full
        if self.capacity == self.counter:
            print("Stack is full")
            return
        
        # change the next of new_node and top of new_node
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.counter += 1
    

    # function to remove an element
    def pop(self):

        # check if the stack is empty
        if self.is_empty():
            return -1
        
        # collect the data from the top
        popped_data = self.top.data
        temp = self.top
        

        # change the pointer of the top
        self.top = self.top.next
        self.counter -= 1
        
        # break the link between the first and second node
        temp.next = None
        # garbage collection
        gc.collect()

        return popped_data
    
    # function to print the stack
    def print_stack(self):
        temp = self.top
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    

if __name__ == "__main__":

    stack = Stack(5)
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)

    stack.push(0)

    stack.print_stack()

    print("Element popped:",stack.pop())
    print("Element popped:",stack.pop())
    print("Now the top element:", stack.peek())
        

        



