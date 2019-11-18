"""Count the number of palindromic substrings"""
def palin_count(s):
    length = len(s)
    dp = [[0 for _ in range(length)] for _ in range(length+1)]

    for i in range(length):
        for j in range(length):
            if i == j:
                dp[i][j] = 1
    
    num_palin = length
    for l in range(1, length):
        print(l)
        for i in range(length - l):
            if s[i] == s[i+l] and l == 1:
                num_palin += 1
                dp[i][i+l] = 1
            elif s[i] == s[i+l] and dp[i+1][i+l-1] == 1:
                num_palin += 1
                dp[i][i+l] = 1
    print(dp[2][3])
    return num_palin

if __name__ == "__main__":
    print(palin_count("abaaba"))



