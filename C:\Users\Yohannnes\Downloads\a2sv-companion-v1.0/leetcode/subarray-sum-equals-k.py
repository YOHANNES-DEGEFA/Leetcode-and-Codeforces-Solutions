class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
    
        cum_sum_to_freq = defaultdict(int)
        cum_sum_to_freq[0] = 1 
        cum_sum  = answer = 0 

        for num in nums: 
            cum_sum += num
            diff = cum_sum -k
    
            if diff in cum_sum_to_freq:
                answer += cum_sum_to_freq[diff] 

            cum_sum_to_freq[cum_sum] += 1

        return answer