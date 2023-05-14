# There are n projects numbered from 0 to n - 1. You are given an integer array milestones where each milestones[i] denotes the number of milestones the ith project has.

# You can work on the projects following these two rules:

# Every week, you will finish exactly one milestone of one project. You must work every week.
# You cannot work on two milestones from the same project for two consecutive weeks.
# Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will stop working. Note that you may not be able to finish every project's milestones due to these constraints.

# Return the maximum number of weeks you would be able to work on the projects without violating the rules mentioned above.

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:

        heap = [-m for m in milestones]
        prev = None
        heapq.heapify(heap)
        weeks = 0
        while heap:
            skip = None
            if heap[0] == prev:
                skip = heapq.heappop(heap)
            if not heap:
                break
            weeks += 1
            curr = heapq.heappop(heap) + 1
            if curr < 0:
                heapq.heappush(heap, curr)
            if skip:
                heapq.heappush(heap, skip)
            prev = curr
        return weeks
