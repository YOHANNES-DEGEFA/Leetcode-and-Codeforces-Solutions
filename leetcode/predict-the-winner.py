class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def f(i,j): 

            if i == j: 
                return nums[i]
            return max(nums[i]-f(i+1,j) , nums[j] - f(i,j-1))
 
        return f(0,len(nums)-1) >= 0 

    
        