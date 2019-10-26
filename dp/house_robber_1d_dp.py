"""House Robber. 1D DP. Time - O(n). Space - O(n)"""
def max_loot(nums):
    length = len(nums)
    dp = [None] * (length + 1)
    dp[0] =  0
    dp[1] = nums[0]
  
    for i in range(2, length + 1):
        dp[i] = max(nums[i-1]+ dp[i-2], dp[i-1])
    return dp[length]

if __name__ == "__main__":
    arr = [1, 2, 3, 1]
    print(max_loot(arr))
