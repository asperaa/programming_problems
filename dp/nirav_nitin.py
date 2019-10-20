"""convert str1 to str2 with min no. of operations like insert, delete, replace"""
def min_cost_dp(str1, str2, m, n):
    # a 2-D array to store the results of sub problems
    dp = [[0 for p in range(n+1)] for p in range(m+1)]
    
    for i in range(m+1):
        for j in range(n+1):

            # if the str1 is empty, then insert all the char
            # of the second string
            if i == 0:
                dp[i][j] == j
            elif j == 0:
                dp[i][j] == i
            elif str1[i-1] == str2[j-2]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], # insert a new char in str1
                                   dp[i-1][j], # delete a new char from str1
                                   dp[i-1][j-1]) # replace a new char from str1
    return dp[m][n]


if __name__ == "__main__":
    str1 = 'nitin'
    str2 = 'nirav'
    m = len(str1)
    n = len(str2)

    print(min_cost_dp(str1, str2, m, n))