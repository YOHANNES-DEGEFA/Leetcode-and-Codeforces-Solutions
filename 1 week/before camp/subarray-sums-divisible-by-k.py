class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixToIndex = defaultdict(int)
        prefixToIndex[0] += 1 
        answer = run_sum = 0 

        for num in nums: 
            run_sum += num 
            mod = run_sum%k 
            if mod in prefixToIndex: 
                answer += prefixToIndex[mod]

            prefixToIndex[mod] += 1 

        return answer 

            
            
        