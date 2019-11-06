"""Counting bits. Time - O(n). Space - O(n)"""
def count_bits(n):
    dp = [None]*(n+1)
    dp[0] = 0
    dp[1] = 1
    if n==1 or n==0:
        return dp[n]

    zone = 0
    for i in range(2, n+1):
        if zone == 0:
            zone = i
            half = zone//2
            half_mover = half
        if half_mover:
            dp[i] = dp[i-half]
            half_mover -= 1
        else:
            dp[i] = dp[i-half] + 1
        zone -= 1
    return dp

if __name__ == "__main__":
    print(count_bits(5))
       
        
        

