"""Longest increasing subsequence. Recursion and Memoization"""
def lis_util(arr, prev_index, curr_index, dp):

    if curr_index == len(arr):
        return 0
    
    if dp[prev_index][curr_index] > -1:
        return dp[prev_index][curr_index]
    
    include_curr = 0

    if prev_index < 0 or arr[prev_index] < arr[curr_index]:
        include_curr = 1 + lis_util(arr, curr_index, curr_index+1, dp)
    not_include_curr = lis_util(arr, prev_index, curr_index+1, dp)

    dp[prev_index+1][curr_index] = max(include_curr, not_include_curr)

    return dp[prev_index+1][curr_index]

def lis(arr):
    if not arr:
        return 0
    length = len(arr)
    dp = [[-1 for _ in range(length)] for _ in range(length+1)]
    return lis_util(arr, -1, 0, dp)

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    arr2 = [1,3,6,7,9,4,10,5,6]

    print(lis(arr2))
