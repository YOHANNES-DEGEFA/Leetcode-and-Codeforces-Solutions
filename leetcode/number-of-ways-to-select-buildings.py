class Solution:
    def numberOfWays(self, s: str) -> int:
        N, answer = len(s), 0
        onesZeros = [[0,0], [0,0]]

        for i in range(N): 
            tmp = int(s[i])

            answer += onesZeros[1][1-tmp]
            onesZeros[1][tmp] += onesZeros[0][1-tmp]
            onesZeros[0][tmp] += 1 

        return answer


       