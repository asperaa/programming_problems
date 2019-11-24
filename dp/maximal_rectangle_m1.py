"""Maximal Rectangle"""

def maximal_rectangle(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    left = [0]*col_len
    right = [0]*col_len
    
    dp = [[0 for _ in range(col_len)] for _ in range(row_len)]

    for i in range(row_len):
        for j in range(col_len):
            dp[i][j] = int(matrix[i][j])

    for j in range(col_len):
        for i in range(1, row_len):
            if dp[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j] + dp[i-1][j]
    maxx = float('-inf')

    for i in range(row_len):
        stack = []
        left = [0]*col_len
        right = [0]*col_len
        for j in range(col_len):
            while stack and dp[i][stack[-1]] >= dp[i][j]:
                stack.pop()
            if stack:
                left[j] = j - stack[-1] - 1
            else:
                left[j] = j
            stack.append(j)
            
        stack = []
        for j in range(col_len-1, -1, -1):
            while stack and dp[i][stack[-1]] >= dp[i][j]:
                stack.pop()
            if stack:
                right[j] = stack[-1] - j
            else:
                right[j] = col_len - j
            stack.append(j)

        for j in range(col_len):
            maxx = max(maxx, dp[i][j]*(left[j]+ right[j]))

    return maxx

if __name__ == "__main__":
    matrix = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    print(maximal_rectangle(matrix))


