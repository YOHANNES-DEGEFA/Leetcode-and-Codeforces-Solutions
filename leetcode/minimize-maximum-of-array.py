class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans  = nums[0]   # coz there is no way to decrease nums[0]

        psum = 0
        i =  1 

        for  i  in range(len(nums)): 
            psum += nums[i]
            windowLen = i + 1
            ans = max(ans, ceil(psum/windowLen))
        return ans 