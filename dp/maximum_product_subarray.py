"""Maximum product subarray"""
def maximum_product(nums):
    if not nums:
        return 0
    length = len(nums)
    dp = [[0 for _ in range(length)] for _ in range(length+1)]
    dp[1] = nums
    maxx = max(nums)
    for i in range(2, length+1):
        for j in range(i-1, length):
            dp[i][j] = dp[i-1][j-1] * nums[j]
            maxx = max(maxx, dp[i][j])

    return maxx

if __name__ == "__main__":
    nums = [-4, -3]
    print(maximum_product(nums)) 