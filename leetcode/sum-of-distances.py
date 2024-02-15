class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        d = {}
        ans = [0]*(len(nums))

        for i, n in enumerate(nums): 
            
            if n in d: 
                d[n].append(i)
            else: 
                d[n] = [i]


        def psum(index): 
            N = len(index)

            cum_sum = [0]*(N+1)

            for i in range(1, N+1): 
                cum_sum[i] += cum_sum[i-1] + index[i-1]

            i = 0
            for idx in index: 
                # jo the key is Here 
                ans[idx] = (i+1)* idx - cum_sum[i] + (cum_sum[-1]-cum_sum[i+1]) -((N-i)*idx)
                i += 1
        

        seen = set()
        for i, n in enumerate(nums): 
            if len(d[n]) > 1 and n not in seen: 
                psum(d[n])

            seen.add(n)

        return ans 
            

        