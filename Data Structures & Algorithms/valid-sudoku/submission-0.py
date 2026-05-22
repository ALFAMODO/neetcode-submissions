class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkUnique(vals: list):
            if len(set(vals))-1 != 9 - vals.count("."):
                return False
            return True

        # check row
        for row in board:
            if not checkUnique(row):
                return False

        for col in range(9):
            column = []
            for row in range(9):
                column.append(board[row][col])
            
            if not checkUnique(column):
                return False
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                grid=[]
                for i in board[row:row+3]:
                    grid.extend(i[col:col+3])
                
                if not checkUnique(grid):
                    return False

        return True
