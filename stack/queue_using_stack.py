"""Implement queue using stack i.e only use stack operations"""
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def empty(self):
        return len(self.s1) == 0
    
    def push(self, val):
        self.s1.append(val)
    
    def pop(self):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        popped = self.s2.pop()
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return popped

    def peek(self):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        topped = self.s2[-1]
        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
        return topped

if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.peek())
