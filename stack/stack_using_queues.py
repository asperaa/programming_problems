"""Implement stack using queues"""

from collections import deque
class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        while len(self.q1) != 0:
            self.q2.append(self.q1.popleft())
        self.q1.append(x)
        while len(self.q2) != 0:
            self.q1.append(self.q2.popleft())

    def pop(self):
        return self.q1.popleft()

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.top()) 