class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
       
        def backtrack(s):
            perms = [] 
            if len(s) == 1: return [s[:]]

            for _ in range(len(s)): 
                num = s.pop(0)
                perm = backtrack(s)

                for p in perm: 
                    p.append(num)

                perms.extend(perm)
                s.append(num)

            return perms
    
        return backtrack(nums)
       