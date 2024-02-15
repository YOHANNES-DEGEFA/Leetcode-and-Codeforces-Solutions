class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        count = [0,0]
        for i in range(len(bills)): 
            note = bills[i]

            if note ==5: 
                count[0] += 1 
            elif note == 10: 
                if not count[0]: 
                    return False
                else: 
                    count[0] -= 1
                count[1] += 1 
                
            else: 
                if not count[0]: 
                    return False
                elif count[0] and count[1]: 
                    count[0] -= 1 
                    count[1] -= 1 
                elif count[0] < 3:
                    return False
                else: 
                    count[0] -= 3 
                   
        return True