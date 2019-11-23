"""Gold mine problem. Naive Recursive approach"""
class GoldMine:
    def __init__(self):
        self.max_gold = 0
    
    def gold_mine_util(self, matrix, curr_sum, i, j, row_len, col_len):
        if i >= row_len or j >= col_len or i < 0:
            return
        if j == col_len - 1:
            curr_sum += matrix[i][j]
            
            self.max_gold = max(self.max_gold, curr_sum)
            return
        
        curr_sum += matrix[i][j]

        self.gold_mine_util(matrix, curr_sum, i, j+1, row_len, col_len)
        self.gold_mine_util(matrix, curr_sum, i+1, j+1, row_len, col_len)
        self.gold_mine_util(matrix, curr_sum, i-1, j+1, row_len, col_len)

        return
    
    def gold_mine(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for i in range(row_len):
            self.gold_mine_util(matrix, 0, i, 0, row_len, col_len)
        return self.max_gold

if __name__ == "__main__":
    # mat = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
    # mat = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
    mat = [[10, 33, 13, 15], [22, 21, 4, 1], [5, 0, 2, 3], [0, 6, 14, 2]]
    GM = GoldMine()
    print(GM.gold_mine(mat))
