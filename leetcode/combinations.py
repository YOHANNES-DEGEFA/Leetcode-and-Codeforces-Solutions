class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        combs = []

        def solve(i, path): 

            if len(path) == k: 
                cur = path[:]
                combs.append(cur)
                return 
            

            for j in range(i+1,n+1): 
                path.append(j)
                solve(j,path)
                path.pop()

        
        solve(0,[])
        return combs