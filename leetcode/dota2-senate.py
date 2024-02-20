class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()
        n = 10 

        for i, v  in enumerate(senate):
            if v == 'R': r.append(i)
            else: d.append(i)

        while d or r:
            if not d: return "Radiant"
            if not r: return "Dire"

            if d.popleft() < r.popleft(): d.append(n)
            else: r.append(n)
            n += 1

        