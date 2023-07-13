# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        hasPre = defaultdict(list)
        hasPreKeys = set()
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
            for c in isPre[curr]:
                if c not in seen:
                    if c not in hasPre:
                        dfs(c)
                    elif c in hasPre:
                        i = len(hasPre[c])
                        for pre in hasPre[c]:
                            if pre in seen:
                                i -= 1
                            else:
                                break
                        if i == 0:
                            dfs(c)
        seen = set()
        for p in noPre:
            dfs(p)
            if len(seen) == numCourses:
                return True
        return False if len(prerequisites) > 1 else True
    

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        required = defaultdict(list)
        for c, req in prerequisites:
            adj[req].append(c)
            required[c].append(req)

        notAvail = set([p[0] for p in prerequisites])
        seen = set()
        def dfs(curr):
            seen.add(curr)
            for p in adj[curr]:
                required[p].remove(curr)
                if p not in seen and not required[p]:
                    dfs(p)

        for i in range(numCourses):
            if i not in notAvail:
                dfs(i)
        return len(seen) == numCourses
