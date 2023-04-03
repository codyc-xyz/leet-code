# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for source, target, time in times:
            heapq.heappush(adj[source], [target, time])

        heap = [[0, k]]
        seen = set()
        while heap:
            time, val = heapq.heappop(heap)
            seen.add(val)
            if len(seen) == n:
                return time
            
            while adj[val]:
                target, travel = heapq.heappop(adj[val])
                heapq.heappush(heap, [time + travel, target])
        return -1

