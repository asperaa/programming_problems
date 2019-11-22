"""Maximal Square"""
def maximal_square(matrix):
    
    row_len = len(matrix)
    col_len = len(matrix[0])

    dp = [[0 for _ in range(col_len)] for _ in range(row_len)]

    maxx = 0
    
    for i in range(row_len):
        dp[i][0] = int(matrix[i][0])
        maxx = max(maxx, dp[i][0])
    
    for j in range(col_len):
        dp[0][j] = int(matrix[0][j])
        maxx = max(maxx, dp[0][j])
    

    for i in range(1, row_len):
        for j in range(1, col_len):
            if matrix[i][j] == "1":
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                maxx = max(maxx, dp[i][j])
    return maxx*maxx

if __name__ == "__main__":
    # matrix = [[0,0,0,0,0], [0,1,1,1,0], [0,1,1,1,0], [0,1,1,1,0], [0,0,0,0,0]]
    matrix = [["0", "1"]]
    print(maximal_square(matrix))