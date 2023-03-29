# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        count = collections.Counter(arr)
        
        counts = []
        for c in count.values():
            counts.append(-c)
        sumCount = len(arr)
        heapq.heapify(counts)
        ans = 0
        while sumCount > len(arr) // 2:
            sumCount += heapq.heappop(counts)
            ans += 1
        return ans