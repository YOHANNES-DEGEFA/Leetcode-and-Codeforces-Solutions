class Solution:
    def bestClosingTime(self, customers: str) -> int:
       N = len(customers) 
       suffix = [0]*(N+1)
       preffix = [0]*(N+1)

       for i in range(N-1,-1,-1): 
           if customers[i] == 'Y': 
               suffix[i] += suffix[i+1] + 1 
           else: 
               suffix[i] = suffix[i+1]

       for j in range(N):
           if customers[j] == "N":
               preffix[j+1] = preffix[j] + 1 
           else: 
               preffix[j+1] = preffix[j]

       minPen = float("inf")
       index = -1
    
       for i in range(N+1):
           curPen = preffix[i] + suffix[i]
           if curPen < minPen:
               # print(i,preffix, suffix)
               index = i 
               minPen  = curPen

       return index 

