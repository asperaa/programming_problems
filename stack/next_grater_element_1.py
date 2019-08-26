"""Find the next greater element in an array"""
class Stack:
    def __init__(self):
        self.s1 = []

def next_great(arr):
    stack = []
    length = len(arr)
    stack.append(arr[-1])
    result = [None]*length
    result[-1] = -1
    for i in range(length-2, -1, -1):
        if len(stack) == 0:
            stack.append(arr[i])
            result[i] = -1
            continue
        if arr[i] < stack[-1]:
            result[i] = stack[-1]
            stack.append(arr[i])
            continue
        while len(stack) != 0 and arr[i] > stack[-1]:
            stack.pop()
        if len(stack) == 0:
            result[i] = -1
            stack.append(arr[i])
        else:
            result[i] = stack[-1]
            stack.append(arr[i])
    
    return result

if __name__ == "__main__":
    arr1 = [4, 3, 2, 1, 5, 6, 9, 10]
    arr2 = [1, 5, 7, 3, 8, 6, 2]
    arr3 = [10, 7, 6, 5, 4, 3, 1]
    arr = [arr1, arr2, arr3]
    for array in arr:
        print(next_great(array))
                

