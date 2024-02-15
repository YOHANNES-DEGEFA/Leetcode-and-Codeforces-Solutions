class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N < 2: 
            return ''
        arr = list(palindrome)
        if palindrome.count('a') == len(palindrome)-1: 
            if palindrome[len(palindrome)//2] != 'a': 
                arr[-1] = 'b'
                return ''.join(arr)

        r = 0 
        while r < N and arr[r] == 'a': 
            r += 1 

        if r == N: 
            arr[-1] = 'b'
        else: 
            arr[r] = 'a'
        
        return ''.join(arr)
        