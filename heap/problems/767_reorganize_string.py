# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = collections.Counter(s)

        heap = []
        for c in count:
            heapq.heappush(heap, [-count[c], c])

        ans = ""
        while heap:
            count2 = None
            count1, char1 = heapq.heappop(heap)
            if not heap and count1 < -1:
                return ""
            if heap:
                count2, char2 = heapq.heappop(heap)
                ans += char1 + char2
            else:
                ans += char1
            if count1 < -1:
                heapq.heappush(heap, [count1 + 1, char1])
            if count2 and count2 < -1:
                heapq.heappush(heap, [count2 + 1, char2])

        return ans


