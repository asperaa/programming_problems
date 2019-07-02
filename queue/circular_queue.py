# circular queue class
class CircularQueue:

    # function to initiate front, rear and capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = self.rear = -1
        self.q = [None]*capacity
    

    # function to add a item to queue
    def enqueue(self, data):

        # check if the queue is full
        if ((self.rear + 1)%self.capacity == self.front):
            print("Queue full.")
        # check if the queue is empty
        elif self.front == -1:
            self.front = self.rear = 0
            self.q[self.rear] = data
        # if the queue is partiallly filled
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.q[self.rear] = data
    
    # function to remove an item from the queue
    def dequeue(self):

        # check if the queue is empty
        if self.front == -1:
            print("Empty queue.")
            return
        # check if the queue has only one element
        elif self.front == self.rear:
            temp = self.q[self.front]
            self.front = self.rear = -1
            return temp
        # the queue is partially filled
        else:
            temp = self.q[self.front]
            self.front = (self.front + 1)%self.capacity
            return temp


if __name__ == "__main__":

    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(3)
    cq.enqueue(4)

    print("Element popped:", cq.dequeue())

