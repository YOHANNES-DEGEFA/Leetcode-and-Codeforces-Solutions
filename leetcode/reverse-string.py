class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def f(s,l,r): 

            if r <= l: 
                return 
            s[r], s[l] = s[l], s[r]

            return f(s,l+1,r-1)

        f(s,0,len(s)-1)
        
            