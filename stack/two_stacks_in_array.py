"""Implement two stacks in an array"""
class TwoStacks:
    def __init__(self, n):
        self.size = n
        self.top1 = -1
        self.top2 = self.size
        self.arr = [None] * self.size
    
    def push1(self, val):
        if self.top2 - self.top1 > 1:
            self.top1 += 1
            self.arr[self.top1] = val
        else:
            print("Stack overflow")
            return False
    
    def push2(self, val):
        if self.top2 - self.top1 > 1:
            self.top2 -= 1
            self.arr[self.top2] = val
            print(self.top2)
        else:
            print("Stack overflow")
            return False
    
    def pop1(self):
        if self.top1 < 0:
            print("Stack empty")
            return False
        popped = self.arr[self.top1]
        self.top1 -= 1
        return popped
    
    def pop2(self):
        if self.top2 > self.size - 1:
            print("stack empty")
            return False
        popped = self.arr[self.top2]
        self.top2 += 1
        return popped

if __name__ == "__main__":
    two_stacks = TwoStacks(6)
    two_stacks.push1(1)
    two_stacks.push1(2)
    two_stacks.push1(3)
    two_stacks.push2(4)
    two_stacks.push2(5)
    two_stacks.push2(6)
    two_stacks.push1(7)
    print(two_stacks.arr)
    two_stacks.pop1()
    print(two_stacks.arr)
    two_stacks.push2(8)
    print(two_stacks.arr)

