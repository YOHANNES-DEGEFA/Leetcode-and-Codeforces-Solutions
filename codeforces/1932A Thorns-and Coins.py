
from functools import lru_cache

@lru_cache(None)
def solve(s, n, i):
    if i >= n or s[i] == '*':
        return 0
    a = 1 if s[i] == '@' else 0
    return a + max(solve(s,n,i+1), solve(s,n,i+2))


for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s, n, 0))