"""Moving average --sliding window"""
from collections import deque
class MovingAverage:
    def __init__(self, size):
        self.queue = deque()
        self.summ = 0
        self.size = size
        self.curr_size = 0
    
    def is_full(self):
        return self.size == len(self.queue)

    def next(self, val):
        if self.is_full():
            if self.queue[0] < 0:
                self.summ += self.queue.popleft()
            else:
                self.summ -= self.queue.popleft()
            self.summ += val
            self.queue.append(val)
            return self.summ / self.size
        self.curr_size += 1

        self.summ += val
        self.queue.append(val)

        return self.summ / self.curr_size

if __name__ == "__main__":
    moving_average = MovingAverage(3)
    print(moving_average.next(1))
    print(moving_average.next(10))
    print(moving_average.next(3))
        