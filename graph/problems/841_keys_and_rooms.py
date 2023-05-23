# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        adj = defaultdict(list)

        for i, keys in enumerate(rooms):
            for k in keys:
                heapq.heappush(adj[i], k)


        seen = [False for _ in range(len(rooms))]

        curr = [0]
        seen[0] = True
        while curr:
            currRoom = heapq.heappop(curr)

            for key in adj[currRoom]:
                if not seen[key]:
                    seen[key] = True
                    curr.append(key)
        
        return True if all(seen) == True else False
