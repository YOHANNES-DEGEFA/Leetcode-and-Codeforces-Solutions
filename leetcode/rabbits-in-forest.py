class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        
        answer = i = 0  
        N = len(answers)


        while i < N:

            tmp  = n = answers[i]
            i += 1
            while  i < N and answers[i] == n and tmp > 0: 
                i += 1 
                tmp -= 1 

                # if (tmp == 0 and i < N) and answer[i+1] == answer[i]: 
                #     i += 1 

            answer += 1 + n 
            

        return answer