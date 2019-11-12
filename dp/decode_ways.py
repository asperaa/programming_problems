"""Number of decodings. DP"""


def num_decodings(s):
    length = len(s)
    if length == 0:
        return 0

    dp = [0 for _ in range(length+1)]
    dp[0] = 1
    
    dp_length = length + 1

    for i in range(1, dp_length):
        if s[i-1] >= "1" and s[i-1] <= "9":
            dp[i] += dp[i-1]
        if i >= 2 and s[i-2:i] >= "10" and s[i-2:i] <= "26":
            dp[i] += dp[i-2]

    return dp[-1]
    

if __name__ == "__main__":
    print(num_decodings("226"))

