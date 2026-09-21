class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows        
        for i in range(9):
            seen = []
            for j in range(9):
                cell = board[i][j]
                if cell != "." and cell in seen:
                    return False
                else:
                    seen += cell
        
        # cols
        for i in range(9):
            seen = []
            for j in range(9):
                cell = board[j][i]
                if cell != "." and cell in seen:
                    return False
                else:
                    seen += cell
        
        for x in range(3):
            for y in range(3):
                seen = []
                for i in range(3):
                    for j in range(3):
                        cell_x = 3 * x + i
                        cell_y = 3 * y + j
                        cell = board[cell_x][cell_y]
                        if cell != "." and cell in seen:
                            return False
                        else:
                            seen += cell
        
        return True