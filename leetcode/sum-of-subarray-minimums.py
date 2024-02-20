class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 1_000_000_007 
        N = len(arr)
        left = [-1] * N
        right = [N] * N 
        result = 0 

        def nextSmallerNumber(arr, lst, flag): 
            stack = []
            if flag == 0: 
                for i in range(len(arr)): 

                    while stack and arr[stack[-1]] >= arr[i]: 
                        lst[stack.pop()] = i 
                        
                    stack.append(i)

                return lst 

            else: 
                for i in range(len(arr)-1,-1,-1): 

                    while stack and arr[stack[-1]] > arr[i]: 
                        lst[stack.pop()] = i 
                        
                    stack.append(i)

                return lst 

        
        right = nextSmallerNumber(arr, right, 0)
        left = nextSmallerNumber(arr, left, 1)
        
        for i, n in enumerate(arr): 
            result += ((i-left[i])*(right[i]-i)*n)%MOD

        return result % MOD