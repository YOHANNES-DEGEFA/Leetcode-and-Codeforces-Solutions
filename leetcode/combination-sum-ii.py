class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res = []

        def dfs(start, s, t):

            if t == 0: 
                res.append(s[:]) 
                return 
            
            if start >= len(c) or t < 0: 
                return 

          
            for i in range(start, len(c)): 
                if i > start and c[i] == c[i-1]: 
                    continue

                s.append(c[i])
                dfs(i+1, s, t-c[i])
                s.pop()
    
               

        dfs(0,[], target)
        return res
    
        