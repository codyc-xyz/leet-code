# You are given a string s consisting of n characters which are either 'X' or 'O'.

# A move is defined as selecting three consecutive characters of s and converting them to 'O'. Note that if a move is applied to the character 'O', it will stay the same.

# Return the minimum number of moves required so that all the characters of s are converted to 'O'.

class Solution:
    def minimumMoves(self, s: str) -> int:
        heap = []

        for i, c in enumerate(s):
            if c == 'X':
                heapq.heappush(heap, i)
        
        if heap:
            init = heap[0]
        else:
            return 0
        ans = 1
        while heap:
            curr = heapq.heappop(heap)
            if curr <= init + 2:
                continue
            else:
                ans += 1
                init = curr
        return ans

        
