class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        #Observations: 

        """
           - if we have n elements we can make n-1 pairs
           - if we are required to divide the array into k , we can actually 
           divide it into k -1 pairs 
           - we only need to focus on the elements that are on the boundaries 

           # Approach 
            - MAKE  a prefix sum of each adjacent pairs   and then sort the 
             the prefix sum and since you can have k - 1 pairs for i 
             in range k - 1 iterate and  
        """
        N = len(weights)
        cum_sum =  [0]*(N-1)

        for i in range(N-1): 
            cum_sum[i] = weights[i] + weights[i+1]

        cum_sum.sort()
        result = 0 
        
        n = N - 1   # n == len cum_sum array 
        for i in range(k-1): 
            result += cum_sum[n-1-i] - cum_sum[i] 

        return result