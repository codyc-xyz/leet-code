# You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

# Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array(i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

# Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums) - 1

        def recurse(l, r):
            if l == r:
                return nums[l]
            max_l = nums[l] - recurse(l + 1, r)
            max_r = nums[r] - recurse(l, r - 1)
            return max(max_r, max_l)

        return recurse(0, N) >= 0


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)

        has_cache = [[False for _ in range(N)] for _ in range(N)]
        cache = [[None for _ in range(N)] for _ in range(N)]

        def recurse(l, r):
            if l == r:
                return nums[l]
            if has_cache[l][r]:
                return cache[l][r]

            max_l = nums[l] - recurse(l + 1, r)
            max_r = nums[r] - recurse(l, r - 1)

            has_cache[l][r] = True
            cache[l][r] = max(max_r, max_l)
            return cache[l][r]

        return recurse(0, N - 1) >= 0
