class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rowMax = [0]*(m)
        colMax = [0]*(n)

        for r in range(m): 
            curMax = 0 
            for c in range(n): 
                if grid[r][c] > curMax: 
                    curMax = grid[r][c]

            rowMax[r] = curMax 

        for c in range(n): 
            curMax = 0 
            for r in range(m): 
                if grid[r][c] > curMax: 
                    curMax = grid[r][c]

            colMax[c] = curMax 

        ans = 0 
        
        for r in range(m): 
            for c in range(n):

                ans += min(colMax[c], rowMax[r])  - grid[r][c]

        return ans 

        
        

        