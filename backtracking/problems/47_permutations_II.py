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

class Solution:
        def permuteUnique(self, nums: List[int]) -> List[List[int]]:      
            ans = []
            path = []
            count = collections.Counter(nums)
            def backtrack(path):
                if len(path) == len(nums) and path not in ans:
                    ans.append(path)
                    return

                elif len(path) >= len(nums):
                    return
                    
                for n in count:
                    if count[n] > 0:
                        count[n] -= 1
                        path.append(n)
                        backtrack(path[:])
                        path.pop()
                        count[n] += 1
            backtrack([])
            return ans