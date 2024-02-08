class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        N = len(nums)
        need = sum(nums) % p
        if need == 0: return 0 

        print(need)

        freq = defaultdict(int)
        freq[0] = -1 
        answer = N 
        run_sum = 0 

        for i , num in enumerate(nums):
            run_sum += num 
            run_sum = run_sum %p 
            diff = run_sum - need 
            diff = diff%p
            if diff in freq: 
                print("HIt")
                answer = min(answer, i-freq[diff])

            freq[run_sum] = i 
       
        return answer if answer < N else -1