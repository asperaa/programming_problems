"""279. Perfect squares"""
def num_squares(n):
    perfect_squres = [i*i for i in range(1, n+1) if i*i <= n]
    dp = [0]*(n+1)

    for i in range(1, n+1):
        for p in perfect_squres:
            sub = i-p
            if sub == 0:
                dp[i] = 1
            elif sub > 0:
                if dp[i] == 0:
                    dp[i] = 1+dp[sub]
                else:
                    dp[i] = min(dp[i], 1+dp[sub])
    return dp[n]

if __name__ == "__main__":
    print(num_squares(7334))