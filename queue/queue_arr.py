# Queue class
class Queue:

    # function to initialise various varibles
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity
        self.Q = [None]*capacity
    
    # function to check whether the queue is full
    def is_full(self):
        if self.size == self.capacity:
            print("Queue is full")
            return True
        return False
    
    # function to check whether is queue is empty
    def is_empty(self):
        if self.size == 0:
            print("Queue is empty")
            return True
        return False
    
    # function to add a new element to the queue
    def en_queue(self, data):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = data
        self.size += 1

    # function to delete a new element to the queue
    def de_queue(self):
        if self.is_empty():
            return
        dequeued_data = self.Q[self.front]
        self.front = (self.front + 1)% self.capacity
        self.size -= 1

        return dequeued_data
    
    # function to show the front of the queue
    def q_front(self):
        if self.is_empty():
            return
        return self.Q[self.front]

    # function to show the end of queue
    def q_rear(self):
        if self.is_empty():
            return
        return self.Q[self.rear]        


if __name__ == "__main__":

    q = Queue(5)
    q.en_queue(5)
    q.en_queue(4)
    q.en_queue(3)
    q.en_queue(2)
    q.en_queue(1)
    q.en_queue(0)

    print(q.q_front())
    print(q.q_rear())

    q.de_queue()

    print(q.q_front())
