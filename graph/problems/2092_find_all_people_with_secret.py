# You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

# Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

# The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

# Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:

        hasSecret = {}
        adj = defaultdict(list)

        for p1, p2, t in meetings:
            heapq.heappush(adj[p1], [t, p2])
            heapq.heappush(adj[p2], [t, p1])

        dq = deque()

        dq.append((0, 0))
        dq.append((firstPerson, 0))
        res = [float('inf') for _ in range(n)]
        res[0] = 0
        res[firstPerson] = 0

        while dq:
            p, t = dq.popleft()
            for time, person in adj[p]:
                if time >= t and res[person] > time:
                    res[person] = time
                    dq.append((person, time))
        
        return [i for i in range(len(res)) if res[i] != float('inf')]