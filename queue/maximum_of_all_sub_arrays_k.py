""""Maximum of all subarrays of size k in an array
Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.
Examples :

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
Output: 3 3 4 5 5 5 6

Input: arr[] = {8, 5, 10, 7, 9, 4, 15, 12, 90, 13}, K = 4
Output: 10 10 10 15 15 90 90"""
from collections import deque

def maximum_sub_array(arr, k):
    queue = deque()
    length = len(arr)
    result = []
    maxx = arr[0]
    for i in range(k):
        if maxx < arr[i]:
            max_index = i
    queue.append(max_index)

    for i in range(k, length):
        result.append(arr[queue[0]])
        while queue and queue[0] < i - k:
            queue.popleft()
        while queue and arr[queue[-1]] < arr[i]:
            queue.pop()
        queue.append(i)
    result.append(arr[queue[0]])
    return result

if __name__ == "__main__":
    arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    print(maximum_sub_array(arr, 4))
    