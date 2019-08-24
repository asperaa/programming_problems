def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, val):
    stack.append(val)
    return val

def pop(stack):
    if is_empty(stack):
        print("stack is empty")
        return -1
    return stack.pop()

if __name__ == "__main__":
    stack = create_stack()
    push(stack, 1)
    push(stack, 2)
    push(stack, 3)
    print(pop(stack))
    print(pop(stack))
    print(pop(stack))
    print(pop(stack))
