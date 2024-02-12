
from collections import defaultdict 

tests = int(input())

for test in range(tests): 
    arrLen = int(input())

    s = input()
    psum = 0
    hashMap = defaultdict(int)
    hashMap[0] = 1 
    res = 0 

    for i, d in enumerate(s): 
        psum += int(d)
        tmp = psum-i-1

        if tmp in hashMap: 
            res += hashMap[tmp]

        hashMap[tmp] += 1 

    print(res)