"""Paint fence

Recurence - num_ways(i) = num_ways_same(i) + num_ways_diff(i)

where:

num_ways_diff(i) = num_ways(i) * (k-1)

num_ways_same(i) = num_ways_diff(i-1) * 1

"""

def paint_fence(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    if n == 2:
        return k*k

    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = k
    dp[2] = k*k
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
    return dp[n]
    
if __name__ == "__main__":
    print(paint_fence(3, 2))