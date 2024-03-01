class Solution:
    def solveNQueens(self, n):
     
        board = [['.']*n for  _ in range(n)]
        res = []

        cols, diag1, diag2  = set(), set(), set()

        def dfs(row): 
            
            if row == n:
                res.append([''.join(r) for r in board])
                return 

            for col in range(n): 
                d1, d2 = row - col, row + col

                if (d1 not in diag1) and (d2 not in diag2) and (col not in cols): 
                    cols.add(col);  diag1.add(d1);  diag2.add(d2)
                    board[row][col]  = 'Q'

                    dfs(row+1)

                    cols.remove(col);  diag1.remove(d1);  diag2.remove(d2)
                    board[row][col] = '.'

        dfs(0)
        return res 


            
