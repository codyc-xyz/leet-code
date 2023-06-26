# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        def dfs(curr, target):
            if curr in seen:
                return
            seen.add(curr)
            if curr == target:
                return True
            if any(dfs(c, target) for c in adj[curr]):
                return True
            return False

        ans = []
        for q1, q2 in queries:
            seen = set()
            if dfs(q1, q2):
                ans.append(True)
            else:
                ans.append(False)

        return ans
