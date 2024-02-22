class Solution:
    def myPow(self, x: float, n: int) -> float:

        def fn(x,n): 
            if n == 0: 
                return 1 

            return x*fn(x*x,n//2) if n % 2 else fn(x*x,n//2)

        if n < 0: 
            return 1/ fn(x,-n)

        return fn(x,n)