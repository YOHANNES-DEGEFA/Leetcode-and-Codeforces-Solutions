
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque()
        soredDeck = sorted(deck,reverse= True)
        
        
        for n in soredDeck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(n)
        return list(d)



