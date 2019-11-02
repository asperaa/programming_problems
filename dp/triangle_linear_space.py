"""Triangle. Linear space and Time - O(n2)"""
def triangle(mat):
    length = len(mat)
    dp = [0]*length
    dp = mat[length-1]

    for k in range(length -2, -1, -1):
        for i in range(k+1):
            dp[i] = min(dp[i], dp[i+1]) + mat[k][i]
    return dp[0]

if __name__ == "__main__":
    mat = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(triangle(mat))