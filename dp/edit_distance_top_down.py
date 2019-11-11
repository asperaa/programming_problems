"""Edit distance. Top down."""
def edit_dist_util(source, dest, m, n, dp):
        if m == 0:
            dp[m][n] = n
            return n
        if n == 0:
            dp[m][n] = m
            return m
        
        if dp[m][n] != -1:
            return dp[m][n]
        
        if source[m-1] == dest[n-1]:
            dp[m][n] = edit_dist_util(source, dest, m-1, n-1, dp)
            return dp[m][n]
        
        insert_opt = 1 + edit_dist_util(source, dest, m, n-1, dp)
        remove_opt = 1 + edit_dist_util(source, dest, m-1, n, dp)
        replace_opt = 1 + edit_dist_util(source, dest, m-1, n-1, dp)

        dp[m][n] = min(insert_opt, remove_opt, replace_opt)
        return dp[m][n]

def edit_dist(source, dest):
    dp = [[-1 for _ in range(len(dest)+1)] for _ in range(len(source)+1)]
    return edit_dist_util(source, dest, len(source), len(dest), dp)

if __name__ == "__main__":
    print(edit_dist("nirav", "nitin"))