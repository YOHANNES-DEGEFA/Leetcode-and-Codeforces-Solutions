class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:


        furthest_dist = 0    
        # find the furthest destination place
        for trip in trips: 
            furthest_dist = max(furthest_dist, trip[2])
        # use the furthest destination + 1 as your cumulative sum array length

        arr_len = furthest_dist + 1
        cum_sum = [0]*(arr_len)
        print(arr_len)
        for numPass, start, end in trips: 
            cum_sum[start] += numPass
            cum_sum[end]   -= numPass

        for i in range(1, arr_len): 
            cum_sum[i] += cum_sum[i-1] 

        if max(cum_sum) <= capacity: 
            return True
        
        return False 
        