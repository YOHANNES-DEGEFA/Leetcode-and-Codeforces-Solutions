n = int(input())
time = list(map(int, input().split()))
time. sort()
psum = 0
ans = 0    #  ans represents the maximum number of not disappointed people

for t in time:
    if psum <= t:
        ans += 1
        psum += t
print(ans)
