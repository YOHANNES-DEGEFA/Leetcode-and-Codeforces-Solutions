class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:


        n = 0      # n = the furthest destination place 
        
        for trip in trips: 
            n = max(n, trip[2])
    
        arr_len = n + 1
        cum_sum = [0]*(arr_len)
      
        for numPass, start, end in trips: 
            cum_sum[start] += numPass
            cum_sum[end]   -= numPass

        for i in range(1, arr_len): 
            cum_sum[i] += cum_sum[i-1] 

        if max(cum_sum) <= capacity: 
            return True
        
        return False 
        