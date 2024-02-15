class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        count = ans = 0
        # count - counts the number of open parenthessis that is not closed yet
        for p in s: 
            if p == '(': 
                count += 1 
            else: 
                if count == 0:
                    ans +=  1 
                    
                count -= 1 
                if count < 0: 
                    count = 0 
     
        return ans   if count < 0 else count + ans 