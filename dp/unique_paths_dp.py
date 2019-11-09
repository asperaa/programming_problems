"""Unique path. DP"""
def unique_path(m, n):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][m-1] = 1
    for j in range(m):
        dp[n-1][j] = 1
    for i in range(n-2, -1, -1):
        for j in range(m-2, -1, -1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]
    return dp[0][0]
    

if __name__ == "__main__":
    print(unique_path(3, 2))