class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:

        target, patches_count, idx = 1, 0, 0 

        while target <= n: 

            if idx < len(nums) and nums[idx] <= target: 
                target += nums[idx]
                idx += 1 
            else: 
                target *= 2 
                patches_count += 1 


        return patches_count
        