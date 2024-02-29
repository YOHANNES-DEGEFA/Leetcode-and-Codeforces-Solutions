class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def gen_subset(start,s): 



            res.append(s[:])
            
            for i in range(start, len(nums)): 
                s.append(nums[i])
                gen_subset(i+1,s)
                s.pop()

        gen_subset(0, [])
        return res