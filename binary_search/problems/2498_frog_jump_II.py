# You are given a 0-indexed integer array stones sorted in strictly increasing order representing the positions of stones in a river.

# A frog, initially on the first stone, wants to travel to the last stone and then return to the first stone. However, it can jump to any stone at most once.

# The length of a jump is the absolute difference between the position of the stone the frog is currently on and the position of the stone to which the frog jumps.

# More formally, if the frog is at stones[i] and is jumping to stones[j], the length of the jump is |stones[i] - stones[j]|.
# The cost of a path is the maximum length of a jump among all jumps in the path.

# Return the minimum cost of a path for the frog.

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        def jump(m):
            ans = 0
            prevF = stones[0]
            for i in range(2, len(stones)):
                if not i % 2 or i == len(stones) - 1:
                    ans = max(ans, stones[i] - prevF)
                    prevF = stones[i]
            for i in range(len(stones) - 1, -1, -1):
                if i % 2 or i == 0:
                    ans = max(ans, prevF - stones[i])
                    prevF = stones[i]
            return ans
        
        l, r = 0, max(stones)
        prevMax = max(stones)
        while l < r:
            m = (l + r) // 2
            res = jump(m)
            if res < prevMax:
                r = m
                prevMax = res
            else:
                l = m + 1
        return prevMax