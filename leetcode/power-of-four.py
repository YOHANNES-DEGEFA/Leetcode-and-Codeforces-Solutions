class Solution:
 
    def isPowerOfFour(self, n: int) -> bool:
        
        def dfs(s): 

            if s == n: 
                return True 
            if n < s: 
                return False 
            
            return dfs(s*4)

        return dfs(1)