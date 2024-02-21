class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
       rows , cols = len(matrix), len(matrix[0])

       # prefixsum each row separetly 
       for row in range(rows): 
           for col in range(1,cols): 
               matrix[row][col] += matrix[row][col-1]
        
       answer = 0 

       for c1 in range(cols): 
           for c2 in range(c1, cols): 
               psum = defaultdict(int)
               psum[0] = 1 

               cur_sum = 0 

               for row in range(rows): 
                   cur_sum += matrix[row][c2] - (matrix[row][c1-1] if c1 > 0 else 0)

                   answer += psum[cur_sum - target]
                   psum[cur_sum]  += 1 

       return answer

        