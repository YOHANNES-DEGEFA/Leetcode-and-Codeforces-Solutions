class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        N = 2*n
        def build(openP, closeP, s): 
            if len(s) == N: 
                res.append(s)
            
            if openP < n: 
                build(openP+1, closeP, s+'(')

            if closeP < openP: 
                build(openP, closeP+1, s+')')

        build(0, 0, '')
        return res