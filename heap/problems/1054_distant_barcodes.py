# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count = collections.Counter(barcodes)
        heap = []
        for c in count:
            heapq.heappush(heap, [-count[c], c])

        ans = []
        while heap:
            cnt1, n1 = heapq.heappop(heap)
            ans.append(n1)
            if heap:
                cnt2, n2 = heapq.heappop(heap)
                ans.append(n2)
                if cnt2 < -1:
                    heapq.heappush(heap, [cnt2 + 1, n2])
            if cnt1 < -1:
                heapq.heappush(heap, [cnt1 + 1, n1])
        return ans
            
