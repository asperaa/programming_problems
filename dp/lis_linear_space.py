"""Longest increasing subsequence"""
def lis(arr):
    if not arr:
        return 0
    length = len(arr)

    dp = [1]*length

    for i in range(length):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], 1+dp[j])
    
    return max(dp)
