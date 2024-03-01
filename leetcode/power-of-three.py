class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        def dfs(s): 
            if n == s: 
                return True 
            if n < s: 
                return False 
            
            s *= 3
            return dfs(s)
            

        return dfs(1)
        