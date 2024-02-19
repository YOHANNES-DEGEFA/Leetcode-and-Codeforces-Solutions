limit = 2*10**5 + 1
psum = [0]*(limit)

def cal(s): 
    n  = len(s)
    ans = 0 
    for i in range(n):
        ans += int(s[i])
        
    return ans 
    
    
for i in range(1, limit):
    psum[i] = cal(str(i))

for i in range(1,limit): 
    psum[i] += psum[i-1]

for _ in range(int(input())): 
    n  = int(input())
    print(psum[n])