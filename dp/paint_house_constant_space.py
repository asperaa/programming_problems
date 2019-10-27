"""Paint house.Time - O(n). Space - O(n)"""
def paint_house(costs):
    if not costs:
        return 0
    
    length = len(costs)
    dp = [[0 for _ in range(3)] for _ in range(length)]
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]

    for i in range(1, length):

        dp[i][0] += (min(dp[i-1][1], dp[i-1][2]) + costs[i][0])
        dp[i][1] += (min(dp[i-1][0], dp[i-1][2]) + costs[i][1])
        dp[i][2] += (min(dp[i-1][0], dp[i-1][1]) + costs[i][2])

    return min(dp[length-1][0], dp[length-1][1], dp[length-1][2])

if __name__ == "__main__":
    costs = [[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]
    print(paint_house(costs))