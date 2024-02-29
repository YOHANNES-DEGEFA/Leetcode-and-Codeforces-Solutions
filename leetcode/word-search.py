class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(i,j,s): 

            if len(s) == 0: 
                return True 
            
            if i< 0 or j < 0 or j>= len(board[0]) or i >= len(board) or s[0] != board[i][j]:  
                return False 
            
            char = board[i][j]
            board[i][j] = '*'

            answer = dfs(i+1,j,s[1:])  or dfs(i,j+1,s[1:]) or dfs(i,j-1, s[1:]) or dfs(i-1,j,s[1:])    

            board[i][j] = char 

            return answer 
     
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                if dfs(i,j,word): 
                    return True
        return False 