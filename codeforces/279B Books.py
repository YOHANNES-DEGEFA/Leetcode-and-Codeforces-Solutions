
n, k = [int(x) for x in input().split()]
a = list(map(int ,input().split()))

l = r = cur_sum = ans =  0

while r < n:
    cur_sum += a[r]
    while cur_sum > k:
        cur_sum -= a[l]
        l += 1

    ans = max(ans, r- l + 1)
    r += 1

print(ans)
