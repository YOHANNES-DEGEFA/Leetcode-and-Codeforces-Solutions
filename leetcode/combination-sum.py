class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
      

        def dfs(target, s, i): 

            if target == 0:
                res.append(s[:]) 
                return

            if target < 0 or i >= len(candidates): 
                return 
          
            s.append(candidates[i])
            dfs(target-candidates[i], s,i)
            s.pop()
            dfs(target, s, i+1)



        dfs(target, [], 0)
        return res
        