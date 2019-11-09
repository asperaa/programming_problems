"""Unique paths"""
class UniquePath:
    def __init__(self):
        self.paths = 0
    
    def unique_path_util(self, i, j, m, n):

        if i == 0 and j == 0:
            self.paths += 1
            return
        
        if i < 0:
            return
        if j < 0:
            return

        self.unique_path_util(i-1, j, m, n)
        self.unique_path_util(i, j-1, m, n)

    def unique_path(self, m, n):
        self.unique_path_util(m-1, n-1, m, n)
        return self.paths

if __name__ == "__main__":
    UniquePath = UniquePath()
    print(UniquePath.unique_path(7, 3))
