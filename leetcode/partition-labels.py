class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        need = Counter(s)
        answer  = []

        def helper(count, need): 

            for k in count: 
                if count[k] != need[k]: 
                    return False
            return True 

        count = Counter()
        l = 0 
        for i, char in enumerate(s): 

            count[char] += 1 
            if helper(count, need): 
                answer.append(i-l+1)

                count = Counter()
                l = i+1

        return answer 

        
        