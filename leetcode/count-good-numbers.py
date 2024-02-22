class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 1_000_000_007
        e, o = n//2 + n%2, n//2 

        def pow(x,n): 
            if n == 0: return 1 
            return (x*pow((x*x)%MOD, n//2))%MOD if n % 2 else (pow((x*x)%MOD, n//2))%MOD

        return (pow(5,e)* pow(4,o))%MOD