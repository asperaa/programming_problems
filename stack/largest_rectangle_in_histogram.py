"""Largest rectangle in a histogram"""
def largest_rectangle(arr):
    length = len(arr)
    left = [None] * length
    right = [None] * length
    stack = []
    for i in range(length):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = i - stack[-1] - 1
        else:
            left[i] = i
        stack.append(i)
    stack = []
    for i in range(length - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1] - i
        else:
            right[i] = length - i
        stack.append(i)
    maxx = 0
    for i in range(length):
        maxx = max(maxx, arr[i]*(left[i] + right[i]))
    return maxx

if __name__ == "__main__":
    # arr = [2, 1, 5, 4, 2, 3, 2, 3]
    arr = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle(arr))
