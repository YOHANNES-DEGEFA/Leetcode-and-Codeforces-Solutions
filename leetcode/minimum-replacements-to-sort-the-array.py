class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        
        N, answer, past  = len(nums), 0, nums[-1]
        nums  = reversed(nums[:-1])
    
        for num in nums: 
            div = int(num/past) + 1 if num % past else int(num/past) 

            answer += div -1 
            past = num//div 

        return answer 