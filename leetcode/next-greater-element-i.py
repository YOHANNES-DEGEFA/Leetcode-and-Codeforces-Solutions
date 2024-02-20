class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        memo = {}
        stack = []    
        # maintain a strictly decreasing monotonic stack 
        for i in range(len(nums2)): 
            while stack and stack[-1] < nums2[i]: 
                memo[stack.pop()] = nums2[i]
            stack.append(nums2[i])
            
      
        answer = [] 
        for num in nums1: 
            answer.append(memo.get(num,-1))

        return answer


    
        