class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        suffix = [0]*(N+1)
        preffix = [0]*(N+1)
        mins = [0]*(N+1)


        for i in range(N): 
            preffix[i+1] = max(preffix[i], height[i])

        for i in range(N-1,-1,-1): 
            suffix[i] = max(suffix[i+1], height[i])

        for i in range(N+1): 
            mins[i]  = min(suffix[i], preffix[i])


        ans = 0 

        for i in range(N): 
            ans += max(0, mins[i]-height[i])

        return ans

        