class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        
        stk = []

        def is_expression(s): 
            return s in ['/','+','-','*']

        def evaluate(num1, num2, exp): 

            if exp == '/':
                return int(num1/num2)
            elif exp == '+':
                return num1 + num2 
            elif exp == '-':
                return num1 - num2 
            else:
                return num1 * num2 
            

        for token in tokens: 
            if is_expression(token): 
                num1 = int(stk.pop())
                num2 = int(stk.pop())


                num = evaluate(num2,num1,token)


                stk.append(str(num))

            else: 
                stk.append(token)

        return int(stk[0])


        

        