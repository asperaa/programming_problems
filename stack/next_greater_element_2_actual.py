"""Find the next greater element if the array is circular"""
def next_greater(arr):
        length = len(arr)
        stack = []
        result = [None] * length
        index = length - 1
        for element in arr[::-1]:
            while stack and stack[-1] <= element:
                stack.pop()
            if stack:
                result[index] = stack[-1]
            else:
                result[index] = -1
            stack.append(element)
            index -= 1
        
        index = length - 1
        print(result)
        print(stack)
        for element in arr[::-1]:
            while stack and stack[-1] <= element:
                stack.pop()
            if stack and result[index] == -1:
                result[index] = stack[-1]
            elif result[index] == -1:
                result[index] = -1
            stack.append(element)
            index -= 1

        return result

if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1]
    print(next_greater(arr))
        