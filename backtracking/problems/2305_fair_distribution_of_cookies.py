# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

# Return the minimum unfairness of all distributions.

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        self.ans = float('inf')
        seen = [False] * len(cookies)
        buckets = [0] * k
        def backtrack(i):
            if max(buckets) >= self.ans:
                return
            if i >= len(seen):
                if False not in seen:
                    self.ans = min(self.ans, max(buckets))
                return
        
            for k in range(i, len(seen)):
                if seen[k]:
                    continue
                for b in range(len(buckets)):
                    buckets[b] += cookies[k]
                    seen[k] = True
                    backtrack(k + 1)
                    buckets[b] -= cookies[k]
                    seen[k] = False
        backtrack(0)
        return self.ans
    

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        buckets = [0] * k
        self.ans = float('inf')
        def backtrack(i, currBucket):
            if i == len(cookies):
                self.ans = min(self.ans, max(currBucket))
                return
            for j in range(k):
                currBucket[j] += cookies[i]
                if currBucket[j] < self.ans:
                    backtrack(i + 1, currBucket)
                currBucket[j] -= cookies[i]

        backtrack(0, buckets)
        return self.ans
            


