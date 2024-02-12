class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        need = len(set(nums))
        unique = defaultdict(int)
        res = 0 

        l = 0 
        for n in nums: 
            unique[n] += 1 

            while len(unique) >= need: 
                unique[nums[l]] -= 1 
                if unique[nums[l]] == 0: 
                    del unique[nums[l]]

                l += 1 
            
            res += l 

        return res 