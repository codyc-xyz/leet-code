# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

class Solution:
        def permuteUnique(self, nums: List[int]) -> List[List[int]]:      
            ans = []
            path = []
            def backtrack(path, seen):
                if len(path) == len(nums) and path not in ans:
                    ans.append(path)
                    return
                elif len(path) == len(nums):
                    return
                for j, c in enumerate(nums):
                    if j not in seen:
                        path.append(c)
                        seen.add(j)
                        backtrack(path[:], seen)
                        path.pop()
                        seen.remove(j)
            backtrack([], set())
            return ans