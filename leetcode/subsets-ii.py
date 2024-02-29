class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def gen_subset(start,s): 

            res.append(s[:])

            for i in range(start,len(nums)): 

                if i > start and nums[i] == nums[i-1]: 
                    continue 
                
                s.append(nums[i])
                gen_subset(i+1,s)
                s.pop()

        gen_subset(0,[])
        return res
        