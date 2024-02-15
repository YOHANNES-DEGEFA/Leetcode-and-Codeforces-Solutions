class Solution:
    def longestPalindrome(self, s: str) -> int:

        count = Counter(s)
        arr = sorted(count.values())
        ans = 0
        atleastOneOdd = 0 

        for num in arr: 
            if num % 2 == 0: 
                ans += num 
            else: 
                ans += num -1 
                atleastOneOdd = 1 
                

        return ans + atleastOneOdd




        