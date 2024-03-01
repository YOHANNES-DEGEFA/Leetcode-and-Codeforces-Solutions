class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0 
        board = [[0]*n for _ in range(n)]
        diag1, diag2, cols = set(), set(), set()

        def dfs(r): 

            if r == n: 
                self.ans += 1 
                return 
            
            for c in range(n): 
                d1, d2 = r-c, r+c 

                if d1 not in diag1 and d2 not in diag2 and c not in cols: 
                    diag1.add(d1);   diag2.add(d2); cols.add(c)
                    board[r][c] = 1

                    dfs(r+1)  

                    diag1.remove(d1);  diag2.remove(d2);  cols.remove(c)
                    board[r][c] = 0 


        dfs(0)
        return self.ans 
