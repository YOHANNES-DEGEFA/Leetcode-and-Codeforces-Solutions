class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        curMin = nums[0]
        stk = []

        for num in nums[1:]: 
            # print(stk,num,curMin)
             

            while stk and stk[-1][1] <= num: 
                stk.pop()

            if stk and  num > stk[-1][0]: 
                return True

            stk.append([curMin, num])
            if num  < curMin: 
                curMin = num 

        return False
