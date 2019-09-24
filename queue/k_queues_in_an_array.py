"""K elements in an array"""
class KQueue:
    def __init__(self, k, n):
        self.arr = [None] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = [i + 1 for i in range(n)]
        self.next[n-1] = -1
        self.free = 0
    
    def is_empty(self, queue):
        return self.front[queue] == -1

    def is_full(self):
        return self.free == -1

    def enqueue(self, queue, val):
        if self.is_full():
            print("queue full")
            return False
        if self.is_empty(queue):
            self.front[queue] = self.free
        self.rear[queue] = self.free
        self.arr[self.free] = val
        self.free = self.next[self.free]
        return True
    
    def dequeue(self, queue):
        if self.is_empty(queue):
            print("Queue empty")
            return False
        new_free = self.front[queue]
        popped = self.arr[new_free]
        if self.front[queue] == self.rear[queue]:
            self.front[queue] = self.rear[queue] = -1
            return popped
        self.front[queue] = self.next[new_free]
        self.next[new_free] = self.free
        self.free = new_free
        return popped

if __name__ == "__main__":
    k_queue = KQueue(3, 10)
    k_queue.enqueue(0, 90)
    k_queue.enqueue(0, 70)
    k_queue.enqueue(0, 80)
    print(k_queue.arr)
    k_queue.enqueue(1, 60)
    print(k_queue.arr)
    print(k_queue.dequeue(1))
    print(k_queue.arr)
    k_queue.enqueue(2, 50)
    print(k_queue.arr)
    print(k_queue.dequeue(2))
    k_queue.enqueue(0, 20)
    k_queue.enqueue(0, 110)
    k_queue.enqueue(2, 75)
    k_queue.enqueue(2, 48)
    print(k_queue.arr)
    print(k_queue.dequeue(0))
    print(k_queue.arr)
    k_queue.enqueue(2, 89)
    print(k_queue.arr)
    print(k_queue.dequeue(1))
    k_queue.enqueue(1, 34)
    print(k_queue.arr)
    k_queue.enqueue(1, 76)
    print(k_queue.dequeue(0))
    k_queue.enqueue(1, 76)
    print(k_queue.arr)


        
