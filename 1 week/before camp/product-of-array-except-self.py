class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix_prod = [1]*(N +1)
        suffix_prod = [1]*(N+1)
        answer = []

        for i in range(N): 
            prefix_prod[i+1] *= prefix_prod[i]*nums[i]
        for i in range(N-1,-1,-1): 
            suffix_prod[i] *= suffix_prod[i+1]*nums[i]
       
        for i in range(N): 
            answer.append(prefix_prod[i] * suffix_prod[i+1])

        return answer 

        

