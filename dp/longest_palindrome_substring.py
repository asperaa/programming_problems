"""Longest palindrome substring"""
def longest_palindrome_substring(s):
    length = len(s)
    dp = [[False for _ in range(length)] for _ in range(length)]

    for i in range(length):
        dp[i][i] = True
    
    indices = (0, 0)
    
    for i in range(length-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            indices = (i, i+1)
    
    step = 2
    for _ in range(length - 2):
        i = 0
        j = step
        while j < length:
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                indices = (i, j)
            i += 1
            j += 1
        step += 1
    
    return s[indices[0]: indices[1]+1]

if __name__ == "__main__":
    s = "babab"
    print(longest_palindrome_substring(s))
            

