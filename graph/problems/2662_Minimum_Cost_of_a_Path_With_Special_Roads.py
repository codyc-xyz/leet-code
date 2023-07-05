# You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

# The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

# There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

# Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:


        q = deque([(start[0], start[1], 0)])
        ans = float('inf')
        while q:
            currX, currY, currCost = q.popleft()
            for startX, startY, endX, endY, cost in specialRoads:
                if cost + abs(currX - startX) + abs(currY - startY) >= abs(endX - currX) + abs(endY - currY) or abs(target[0] - currX) + abs(target[1] - currY) <= abs(target[0] - endX) + abs(target[1] - endY):
                    continue
                q.append([endX, endY, currCost + cost + abs(currX - startX) + abs(currY - startY)])
            ans = min(ans, currCost + abs(target[0] - currX) + abs(target[1] - currY))
        return ans

            
