"""Coin Change. Bottom up"""
def coin_change(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    
    for i in range(1, amount+1):
        for j in range(len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i - coins[j]]+1)
    
    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]

if __name__ == "__main__":
    coins = [1, 2, 5]
    print(coin_change(coins, 100)) 