"""Buy and sell stock. O(n) and O(1). No DP."""
def max_profit(prices):
    min_so_far = prices[0]
    max_profit_so_far = float('-inf')
    for price in prices:
        min_so_far = min(price, min_so_far)
        max_profit_so_far = max(max_profit_so_far, price - min_so_far)
    
    return max_profit_so_far

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))