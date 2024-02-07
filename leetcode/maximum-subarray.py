class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = ans = float('-inf')

        for num in nums:
            curSum = max(curSum+num, num)
            ans = max(ans, curSum)

        return ans 
        