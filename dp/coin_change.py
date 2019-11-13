"""Coin change. Top down. 1D DP."""
class CoinChange:
    
    def coin_change_util(self, coins, amount, dp):
        if amount < 0:
            return -1
        if dp[amount] != -1:
            return dp[amount]
        if amount == 0:
            dp[amount] = 0
            return 0
        minn = float('inf')
        for i in range(len(coins)):
            num_coins = 1 + self.coin_change_util(coins, amount-coins[i], dp)
            if num_coins >= 1:
                minn = min(minn, num_coins)
        if minn != float('inf'):
            dp[amount] = minn
        else:
            dp[amount] = -1

        return dp[amount]
    
    def coin_change(self, coins, amount):
        dp = [-1]*(amount+1)
        num_coins =  self.coin_change_util(coins, amount, dp)
        return num_coins


if __name__ == "__main__":
    coins = [1, 2, 5]
    CC = CoinChange()
    print(CC.coin_change(coins, 100)) 