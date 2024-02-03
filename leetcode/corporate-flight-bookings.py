class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cum_sum = [0]*(n+1)

        for left, right, seats in bookings: 
            cum_sum[left-1] += seats     # left -1 because our array is 0-indexed 
            cum_sum[right] -= seats    
        for i in range(1,n+1): 
            cum_sum[i] += cum_sum[i-1]

        return cum_sum[:-1]

        