class Solution:
    def minimumSteps(self, s: str) -> int:

        l = r = answer = 0 
        n = len(s)
        s = list(s)
        

        while r < n: 
            while l < r and s[l] == '0':
                l += 1
            while r < n and s[r] == '1': 
                r += 1
            if r == n: 
                break 
            s[l], s[r] = s[r], s[l]
            answer += r-l
            r += 1
            l += 1 

        return answer