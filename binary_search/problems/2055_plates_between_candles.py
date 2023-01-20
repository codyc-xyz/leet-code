# There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

# You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

# For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

# Return an integer array answer where answer[i] is the answer to the ith query.

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pSum = []
        candles = []
        nearestLCandle = []
        nearestRCandle = deque()
        ans = []
        count = 0
        for i, c in enumerate(s):
            if c == '*':
                count += 1
            else:
                candles.append(i)
            if candles:
                nearestLCandle.append(candles[-1])
            else:
                nearestLCandle.append(None)
            pSum.append(count)
        j = 0
        for i in range(len(s)):
            
            if j < len(candles) and i < candles[j]:
                nearestRCandle.append(candles[j])
            elif j < len(candles) and i == candles[j]:
                nearestRCandle.append(candles[j])
                j += 1
            else:
                nearestRCandle.append(None)
      
        for q in queries:
            l, r = q[0], q[1]
            
            left, right = nearestRCandle[l], nearestLCandle[r]
            if left != None and right != None and right > left:
                ans.append(pSum[right] - pSum[left])
            else:
                ans.append(0)
        return ans

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        pSum = []
        candles = []
        ans = []
        count = 0
        for idx, i in enumerate(s):
            if i == '*':
                count += 1
            else:
                candles.append(idx)
            pSum.append(count)
        for q in queries:
            
            l, r = q[0], q[1]
            
            left = bisect_left(candles, l)
            right = bisect_right(candles, r) - 1
            if left < right:
                ans.append(pSum[candles[right]] - pSum[candles[left]])
            else:
                ans.append(0)
        return ans