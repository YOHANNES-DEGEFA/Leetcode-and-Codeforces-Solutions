class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
       N = len(nums)
       n = N+1
       prefix = [0]*n
       suffix = [0]*n
       result = [0]*N
       for i in range(N):
           prefix[i+1] = prefix[i]+nums[i]
       
       for j in range(N-1,-1,-1):
           suffix[j] = suffix[j+1]+nums[j]
       
       
       for i in range(N):
           absDiff = (i*nums[i]-prefix[i]) + abs((N-i)*nums[i] - suffix[i])
           result[i] = absDiff
       return result 
        
        