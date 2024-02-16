class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        for b in s: 
            if b in ["{", "[", "("]: 
                stk.append(b)

            else: 

                if not stk: 
                    return False 

                p = stk.pop()
                if p == '{' and b != '}': 
                    return False
                elif p == '(' and b != ')': 
                    return False 
                elif p == '[' and b != ']': 
                    return False 
                



        return True if not stk else False