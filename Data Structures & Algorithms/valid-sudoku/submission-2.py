class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".": continue

                if val in rows[i] or val in cols[j] or val in grids.get((i//3, j//3), set()):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                grids.setdefault((i//3,j//3), set()).add(val)

        return True    
                

                  
        
