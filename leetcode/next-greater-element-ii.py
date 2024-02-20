class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        n = len(nums)
        answer = [-1]*(n)

        for i in range(n*2): 
            while stack and nums[stack[-1]] < nums[i%n]: 
                answer[stack.pop()] = nums[i%n]
            stack.append(i%n)
            
        return answer 

        