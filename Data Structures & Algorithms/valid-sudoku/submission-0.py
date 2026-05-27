class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        for row in board:
            seen = set()
            for item in row:
                if item != ".":
                    if item in seen:
                        return False
                    seen.add(item)
        for i in range(n):
            seen = set()
            for j in range(n):
                item = board[j][i]
                if item != ".":
                    if item in seen:
                        return False 
                    seen.add(item)    
        em_all = [set() for _ in range(n)]                       
        for i in range(n):
            for j in range(n):
                N = (i//3*3+j//3)
                square = em_all[N]
                item = board[i][j]

                if item != ".":
                    if item in square:
                        return False
                    em_all[N].add(item)    


        return True                
        