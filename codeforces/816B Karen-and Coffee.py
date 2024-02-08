n, k, q = [int(x) for x in input().split()]
 
psum = [0]*(200002)
 
for _ in range(n):
    l, r = [int(x) for x in input().split()]
    psum[l] += 1
    psum[r+1] -= 1
 
run_sum  = 0
for i in range(1,200002):
    run_sum += psum[i]
    psum[i] = 1 if run_sum >= k else 0
 
for i in range(1,200002):
    psum[i] += psum[i-1]
 
 
for _ in range(q):
    l, r = [int(x) for x in input().split()]
    ans = psum[r] - psum[l-1]
    print(ans)