class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [x for x in range(1,10)]
        res = []

        def dfs(i,n, s): 

            if n == 0 and len(s) == k: 
                res.append(s[:])
                return 


            if i > 8 or len(s) > k: 
                return 

            s.append(nums[i])
            dfs(i+1,n-nums[i],s)
            s.pop()

            dfs(i+1, n, s)

        dfs(0,n,[])
        return res 

