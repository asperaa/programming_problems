"""Min cost climbing stairs. DP. Time - O(n). Space - O(n)"""
def min_cost(costs):
    length = len(costs)
    dp = [None] * (length + 1)
    dp[0] = costs[0]
    dp[1] = costs[1]

    for i in range(2, length):
        dp[i] = min(dp[i-1] + costs[i], dp[i-2] + costs[i])

    dp[length] = min(dp[length-1], dp[length-2])

    return dp[length]

if __name__ == "__main__":
    costs = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(min_cost(costs))