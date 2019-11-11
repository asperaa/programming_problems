"""Minimum path sum"""
def minimum_path_sum_util(grid, m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[m-1][n-1] = grid[m-1][n-1]

    for i in range(m-2, -1, -1):
        dp[i][n-1] = (dp[i+1][n-1] + grid[i][n-1])

    for j in range(n-2, -1, -1):
        dp[m-1][j] = dp[m-1][j+1] + grid[m-1][j]
    
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

    return dp[0][0]

def path_sum(grid):
    m = len(grid)
    if m:
        n = len(grid[0])
    else:
        n = 0
    return minimum_path_sum_util(grid, m, n)

if __name__ == "__main__":
        grid = [
          [1,3,1],
          [1,5,1],
          [4,2,1]
          ]
        # grid = [[1, 2], [1, 1]]
        print(path_sum(grid))