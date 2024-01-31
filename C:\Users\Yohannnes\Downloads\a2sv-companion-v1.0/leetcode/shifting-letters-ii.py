class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shifts_sum = [0]*(len(s)+1)

        for start, end, direction in shifts: 
            if direction == 0: 
                shifts_sum[start] -= 1 
                shifts_sum[end+1] += 1     # end + 1 because end is inclusive 
            else: 
                shifts_sum[start] += 1 
                shifts_sum[end+1] -= 1


        cum_sum = 0
        shifts_list = []

        for i, char  in enumerate(s): 
            cum_sum += shifts_sum[i]
            cur_shift = (cum_sum + ord(char)-97)%26 + 97
            
            shifts_list.append(chr(cur_shift))

        return ''.join(shifts_list)


