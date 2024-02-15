class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x: x[1]) 

        l = r = answer = 0 
        N = len(points)
        

        while r < N: 
            l = r 
           
            while r < N and points[r][0] <= points[l][1]: 
                r += 1 
            answer += 1 

        return answer 
        