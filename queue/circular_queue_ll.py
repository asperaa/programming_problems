import gc

class Node:

    # function to add a new node
    def __init__(self, data):
        self.data = data
        self.link = None

class CircularQueue:

    # function to initiate front and rear
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        
        # create a new node and fill it with data
        new_node = Node(data)
        
        # check if the queue is empty
        if self.front == None:
            self.front = new_node
        # check if the node is partially filled
        else:
            self.rear.link = new_node
        
        self.rear = new_node
        self.rear.link = self.front
    
    def dequeue(self):

        if self.front == None:
            print("Queue Empty.")
            return
        # save the front item
        temp = self.front
        data_popped = temp.data
        
        # move the front pointer forward
        self.front = temp.link

        temp.link = None
        gc.collect()

        self.rear.link = self.front

        return data_popped

    def print_queue(self):

        temp = self.front
        while(temp.link != self.front):
            print(temp.data, end=" ")
            temp = temp.link
        print(temp.data, end=" ")
        print()
    
if __name__ == "__main__":
    cq = CircularQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(4)
    cq.enqueue(5)

    cq.print_queue()
    print("Popped:", cq.dequeue())

    cq.print_queue()


        
