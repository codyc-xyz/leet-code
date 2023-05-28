# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        hasPre = defaultdict(list)
        isPre = defaultdict(list)
        noPre = set()
        for c, pre in prerequisites:
            hasPre[c].append(pre)
            isPre[pre].append(c)

        for i in range(numCourses):
            if i not in hasPre:
                noPre.add(i)


        def dfs(curr):
            seen.add(curr)
            ans.append(curr)

            for c in isPre[curr]:
                if c not in seen:
                    i = len(hasPre[c])
                    for p in hasPre[c]:
                        if p in seen:
                            i -= 1
                        else:
                            break
                    if i == 0:
                        dfs(c)

        ans = []
        seen = set()
        for p in noPre:
            if p not in seen:
                dfs(p)
        return ans if len(seen) == numCourses else []
