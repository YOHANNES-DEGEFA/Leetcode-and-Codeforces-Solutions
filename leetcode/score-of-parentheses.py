class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []

        for p in s: 
            if p == "(": 
                stk.append(0)

            else: 
                tmp = stk.pop()
                if tmp == 0: 
                    tmp = 1 
                else: 
                    tmp *= 2 

                if stk: 
                    stk[-1] += tmp 
                else: 
                    stk.append(tmp)
                
        return stk.pop()

        # ans = 0
        # stk = []
        # x = 0
        # for p in s: 
        #     if p == '(':

        #         if x > 0:
        #             num = 2**(x-1) 
        #             if stk: 
        #                 if type(stk[-1]) == type(1): 
        #                     stk.append(stk.pop()+num)
        #                 else: 
        #                     stk.append(num)
        #             else: 
        #                 ans += 2**(x-1) 
                    
        #         stk.append(p)
        #         x = 0
        #     else:
        #         x += 1 
        #         stk.pop()

        # if x > 0:
        #     ans += 2**(x-1)  
        # return ans 


        