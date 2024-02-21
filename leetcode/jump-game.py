class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = 0    # best represents the furthest index we can reach 
        N = len(nums)

        for i, n in enumerate(nums):
            if i + n > best:
                best = i + n

            if n == 0 and best <= i and best < N-1:
                return False
        return True