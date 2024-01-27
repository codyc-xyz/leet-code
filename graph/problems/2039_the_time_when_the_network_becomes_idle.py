# There is a network of n servers, labeled from 0 to n - 1. You are given a 2D integer array edges, where edges[i] = [ui, vi] indicates there is a message channel between servers ui and vi, and they can pass any number of messages to each other directly in one second. You are also given a 0-indexed integer array patience of length n.

# All servers are connected, i.e., a message can be passed from one server to any other server(s) directly or indirectly through the message channels.

# The server labeled 0 is the master server. The rest are data servers. Each data server needs to send its message to the master server for processing and wait for a reply. Messages move between servers optimally, so every message takes the least amount of time to arrive at the master server. The master server will process all newly arrived messages instantly and send a reply to the originating server via the reversed path the message had gone through.

# At the beginning of second 0, each data server sends its message to be processed. Starting from second 1, at the beginning of every second, each data server will check if it has received a reply to the message it sent (including any newly arrived replies) from the master server:

# If it has not, it will resend the message periodically. The data server i will resend the message every patience[i] second(s), i.e., the data server i will resend the message if patience[i] second(s) have elapsed since the last time the message was sent from this server.
# Otherwise, no more resending will occur from this server.
# The network becomes idle when there are no messages passing between servers or arriving at servers.

# Return the earliest second starting from which the network becomes idle.

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        n = len(patience)
        adj = defaultdict(list)

        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        q = deque()
        res = [float('inf') for _ in range(n)]
        q.append((0, 0))
        seen = set()
        seen.add(0)
        while q:
            curr, hops = q.popleft()
            res[curr] = hops * 2
            for n in adj[curr]:
                if n not in seen:
                    q.append((n, hops + 1))
                    seen.add(n)

        ans = max(res)
        for i, r in enumerate(res):
            if i == 0:
                continue
            diff = r
            if r % patience[i] == 0:
                diff -= patience[i]
            else:
                diff -= (r % patience[i])
            ans = max(ans, r + diff)
        return ans + 1
              