class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_opreations = 0 

        while maxDoubles and target > 1:
            min_opreations += 1 + target % 2 
            target //= 2    # use bits to divide into half efficiently 
            maxDoubles -= 1 

        return target + min_opreations -1 