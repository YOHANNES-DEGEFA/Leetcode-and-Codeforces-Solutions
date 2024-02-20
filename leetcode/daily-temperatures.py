class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [0]*(N)
        stack = [] 
      
        for i , n in enumerate(nums): 
            while stack and  nums[stack[-1]] < n: 
                idx = stack.pop()
                answer[idx] =  i - idx

            stack.append(i)
            
        return answer 
