"""Queue implementation of array"""
class Queue:
    def __init__(self, capacity):
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.capacity = capacity
        self.Q = [None] * self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.capacity
    
    def q_front(self):
        if self.is_empty():
            print("Empty queue")
            return False
        return self.Q[self.front]
    
    def q_rear(self):
        if self.is_empty():
            print("Empty queue")
            return False
        return self.Q[self.rear]
    
    def de_queue(self):
        if self.is_empty():
            print("Empty queue")
            return False
        de_queued_element = self.Q[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1 
        return de_queued_element
    
    def en_queue(self, val):
        if self.is_full():
            print("Queue full")
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = val
        self.size += 1
        return True

if __name__ == "__main__":
    Q = Queue(4)
    Q.en_queue(1)
    Q.en_queue(2)
    Q.en_queue(3)
    Q.en_queue(4)
    Q.de_queue()
    Q.en_queue(5)
    print(Q.Q)