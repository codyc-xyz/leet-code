# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

# You must find the minimum number of months needed to complete all the courses following these rules:

# You may start taking a course at any time if the prerequisites are met.
# Any number of courses can be taken at the same time.
# Return the minimum number of months needed to complete all the courses.

# Note: The test cases are generated such that it is possible to complete every course(i.e., the graph is a directed acyclic graph).

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        if n == 1:
            return time[0]
        monthsTaken = defaultdict(int)

        for i, t in enumerate(time):
            monthsTaken[i+1] = t

        reqs = defaultdict(set)
        reqFor = defaultdict(set)
        for start, end in relations:
            reqs[end].add(start)
            reqFor[start].add(end)

        heap = []
        for i in range(1, n + 1):
            if not reqs[i]:
                heapq.heappush(heap, [monthsTaken[i], i])

        ans = 0
        seen = set()

        while heap:
            currTime, curr = heapq.heappop(heap)
            if curr not in seen:
                seen.add(curr)
                if len(seen) == n:
                    return currTime
                for r in reqFor[curr]:
                    reqs[r].remove(curr)
                    if not reqs[r]:
                        heapq.heappush(heap, [currTime + monthsTaken[r], r])
