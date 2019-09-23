"""K stacks in an array"""
class K_Stack:
    def __init__(self, n, k):
        self.arr = [None] * n
        self.tops_of_stacks = [-1] * k
        self.free = 0
        self.next = [i + 1 for i in range(n)]
        self.next[n-1] = -1

    def is_empty(self, stack):
        return self.tops_of_stacks[stack] == -1
    
    def is_full(self):
        return self.free == -1

    def push(self, stack, val):
        if self.is_full():
            print("Stack full")
            return False
        old_top = self.tops_of_stacks[stack]
        self.tops_of_stacks[stack] = self.free
        new_top = self.tops_of_stacks[stack]
        self.arr[new_top] = val
        self.free = self.next[new_top]
        self.next[new_top] = old_top
    
    def pop(self, stack):
        if self.is_empty(stack):
            print("Stack empty")
            return False
        old_top = self.tops_of_stacks[stack]
        new_top = self.next[old_top]
        
        popped = self.arr[old_top]
        self.tops_of_stacks[stack] = new_top
        self.free = old_top

        return popped

if __name__ == "__main__":
    k_stacks = K_Stack(9, 3)
    k_stacks.push(0, 1)
    k_stacks.push(1, 2)
    k_stacks.push(2, 3)
    k_stacks.push(0, 4)
    k_stacks.push(0, 5)
    k_stacks.push(0, 6)
    k_stacks.push(1, 7)
    k_stacks.push(2, 9)
    k_stacks.push(2, 10)
    print(k_stacks.pop(1))
    print(k_stacks.pop(1))
    print(k_stacks.pop(0))

        

    