"""Triangle. Space - O(n2). Time - O(n2)"""
def triangle(mat):
    length = len(mat)
    dp = [[0 for _ in range(length)] for _ in range(length)]
    dp[length-1] = mat[length-1]
    
    for k in range(length -2, -1, -1):
        for i in range(len(mat[k])):
            dp[k][i] = min(dp[k+1][i], dp[k+1][i+1]) + mat[k][i]
    
    return dp[0][0]


if __name__ == "__main__":
    mat = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(triangle(mat))