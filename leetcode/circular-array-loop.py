class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        N = len(nums)
        move = lambda x: (x + nums[x]) % N

        for i, num in enumerate(nums):
            if num == 0:
                continue

            slow = i
            fast = move(i)

            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[move(fast)] > 0:
                if fast == slow:

                    if slow == move(slow):
                        break
                    return True

                slow = move(slow)
                fast = move(move(fast))

            add = i

            while nums[add] * nums[move(add)] > 0:
                
                tmp = add
                add = move(add)
                nums[tmp] = 0
        return False
            


        