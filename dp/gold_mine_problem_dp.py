"""Gold mine problem"""

def gold_mine(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    
    dp = [[0 for _ in range(col_len)] for _ in range(row_len)]
    
    for i in range(row_len):
        dp[i][col_len-1] = matrix[i][col_len-1]
    maxx = float('-inf')
    for j in range(col_len - 2, -1, -1):
        for i in range(row_len):
            if i == 0:
                dp[i][j] = matrix[i][j] + max(dp[i][j+1], dp[i+1][j+1])
            elif i == row_len - 1:
                dp[i][j] = matrix[i][j] + max(dp[i][j+1], dp[i-1][j+1])
            else:
                dp[i][j] = matrix[i][j] + max(dp[i][j+1], dp[i+1][j+1], dp[i-1][j+1])
        
            maxx = max(maxx, dp[i][j])
    return maxx

if __name__ == "__main__":
    # mat = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
    mat = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
    # mat = [[10, 33, 13, 15], [22, 21, 4, 1], [5, 0, 2, 3], [0, 6, 14, 2]]

    print(gold_mine(mat))
