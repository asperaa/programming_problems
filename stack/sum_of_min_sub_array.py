"""Find the sum of min element of each sub-array"""
def min_sub_array(arr):
    length = len(arr)
    left = [-1] * length
    right = [length] * length
    stack = []

    for i in range(length):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            left[i] = i + 1
        else:
            left[i] = i - stack[-1]
        stack.append(i)
    left[0] = 1
    
    stack = []

    for i in range(length - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            right[i] = length - i
        else:
            right[i] = stack[-1] - i
        stack.append(i)
    right[-1] = 1
    summ = 0
    modd = 10**9 +7
    for i in range(length):
        summ = (summ + arr[i]*left[i]*right[i]) % modd

    return left, right, summ

if __name__ == "__main__":
    # arr = [2, 9, 7, 8, 3, 4, 6, 1]
    arr = [3, 1, 2, 4, 2 ]
    print(min_sub_array(arr))
