class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        prefix_sum = [0]*(N)
        suffix_sum = [0]*(N+1)
        prefix_sum[0] = s[0] == '0'
        for i in range(1,N): 
            prefix_sum[i] += prefix_sum[i-1] + int(s[i]=='0' )

        for j in range(N-1,-1,-1): 
            suffix_sum[j] += suffix_sum[j+1] + int(s[j] == '1')

        max_score = 0 
        for i in range(N-1): 
            max_score = max(max_score, suffix_sum[i+1]+prefix_sum[i])

        return max_score