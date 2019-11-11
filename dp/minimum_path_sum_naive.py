"""Minimum path sum. Naive"""
class MinPathSum:
    def __init__(self):
        self.min_path_sum = float('inf')

    def path_sum_util(self, grid, i, j, m, n, path_sum):
        if i == m-1 and j == n-1:
            path_sum += grid[i][j]
            print(path_sum, i, j)
            self.min_path_sum = min(self.min_path_sum, path_sum)
            print("New path")
            return
        if i > m-1:
            return
        if j > n-1:
            return
        path_sum += grid[i][j]
        print(path_sum, i, j)
        self.path_sum_util(grid, i, j+1, m, n, path_sum)
        self.path_sum_util(grid, i+1, j, m, n, path_sum)
    
    def path_sum(self, grid):
        m = len(grid)
        if m:
            n = len(grid[0])
        else:
            n = 0
        self.path_sum_util(grid, 0, 0, m, n, 0)
        return self.min_path_sum

if __name__ == "__main__":
        # grid = [
        #   [1,3,1],
        #   [1,5,1],
        #   [4,2,1]
        # ]
        grid = [[1, 2], [1, 1]]
        MPS = MinPathSum()
        print(MPS.path_sum(grid))
        