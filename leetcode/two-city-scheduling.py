class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs.sort(key= lambda x: x[0]-x[1])

        l, r = 0, len(costs)-1 
        min1 = min2 = 0
        n = len(costs)//2
        for i in range(n): 
            min1 +=  costs[i][0]

        for j in range(n,2*n): 
            min2 += costs[j][1]


        return min1 + min2

        