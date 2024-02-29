class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = { '2': 'abc', '3': "def", '4': 'ghi', '5': 'jkl', 

                        '6': 'mno', '7': 'pqrs' , '8': 'tuv', '9': 'wxyz'
        }
        if not digits: 
            return 
        res = []
        def dfs(i,s):

            if len(s) == len(digits): 
                res.append(s)
                return 

            for c in digitToChar[digits[i]]: 
                dfs(i+1, s + c)


        dfs(0,'')
        return res 
