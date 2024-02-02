class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        hashMap, unique_elem = defaultdict(int), len(set(nums))
        ans, l = 0, 0 
        for r in range(len(nums)):
            hashMap[nums[r]] += 1 
            while len(hashMap) == unique_elem:
                hashMap[nums[l]] -= 1 
                if not hashMap[nums[l]]:  # if it is zero
                    del hashMap[nums[l]]
                l += 1

            ans += l 
        return ans 

            















        # setLen= len(set(nums))
        # N = len(nums)
        # res = 0
        # l, r = 0, 0
        # for i in range(N):
        #     tempSet = set(nums[i])
        #     for j in range(i+1,N):
        #         if len(tempSet) == setLen:
        #             res += 1

        #         tempSet.add(nums[j])

        #         if j == 

        