class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i, n in enumerate(tickets): 
            queue.append([n,i])
        ans = 0 
        while True: 
            queue[0][0] -= 1 
            ans += 1
            if queue[0][0] == 0: 
                if  queue[0][1] != k: 
                    queue.popleft() 
                else: 
                    return ans
            else: 
                queue.append(queue.popleft())
                


        