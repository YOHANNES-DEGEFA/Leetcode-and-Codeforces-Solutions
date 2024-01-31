class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        N = len(nums)
        cum_sum = [0]*(N+1)
        nums.sort()
        mod = 10**9 + 7

        for left, right in requests: 
            cum_sum[left]    += 1 
            cum_sum[right+1] -= 1 

        for i in range(1,N): 
            cum_sum[i] += cum_sum[i-1]

        cum_sum.sort()
        
        answer = 0 
        while nums: 
            answer += cum_sum.pop() * nums.pop()

        return answer%mod
        