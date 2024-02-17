class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')

        stk = []
        for file in arr: 
            if file == '..': 
                if stk: 
                    stk.pop()

            elif file == '.' or file=="": 
                continue
            else: 
                stk.append(file)

        return "/"+'/'.join(stk)

