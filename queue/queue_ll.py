import gc
# class Queue
class Node:

    # function to initiate the data filling and next part
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class
class Queue:

    # function to initiate the front and rear pointers of queue
    def __init__(self):
        self.front = None
        self.rear = None
    

    # function to check whether the queue is empty
    def is_empty(self):
        return self.front == None

    # function to enqueue
    def enqueue(self, data):
        
        # create a new node and fill it with data
        new_node = Node(data)

        # check if the the queue is empty
        if self.rear is None:
            self.rear = self.front = new_node
            return
        
        self.rear.next = new_node
        self.rear = new_node
    

    # function to delete a dequeue
    def dequeue(self):

        if self.is_empty():
            return
        
        # store the first node in a temp var
        temp = self.front
        
        # store the popped data
        popped_data = temp.data

        # change the front of queue to the second node
        self.front = temp.next

        # change the next of temp node to null
        temp.next = None

        # do garbage collection
        gc.collect()

        return popped_data
    

if __name__ == "__main__":

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("Element popped:", q.dequeue())



