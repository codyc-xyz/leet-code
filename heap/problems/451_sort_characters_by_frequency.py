# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

class Solution:
    def frequencySort(self, s: str) -> str:

        count = collections.Counter(s)
        heap = []
        for char in count:
            heap.append([count[char], char])
        
        heapq.heapify(heap)
        ans = ""

        while heap:
            count, char = heapq.heappop(heap)
            while count > 0:
                ans = char + ans
                count -= 1
        return ans