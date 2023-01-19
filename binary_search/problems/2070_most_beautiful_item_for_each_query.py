# You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

# You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

# Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        
        items.sort(key=lambda x: (x[0], x[1]))
        maxNum = 0
        maxNums = []
        for i in items:
            if i[1] > maxNum:
                maxNum = i[1]
            maxNums.append(maxNum)
        
        price_list = [i[0] for i in items]
        for q in queries:
            idx = bisect_right(price_list, q)
            if 0 < idx <= len(items):
                ans.append(maxNums[idx - 1])
            else:
                ans.append(0)
        return ans