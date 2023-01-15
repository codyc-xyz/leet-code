# You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

# The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

# Return the maximum tastiness of a candy basket.

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def isValid(K, m):
            prev = price[0]
            for i in range(1, len(price)):
                if price[i] - prev >= m:
                    K -= 1
                    prev = price[i]
            return K <= 0
        
        l, r = 0, max(price) - min(price)
        ans = 0
        while l <= r:
            m = (l + r) // 2
            K = k - 1
            if isValid(K, m):
                l = m + 1
                ans = m
            else:
                r = m - 1
        return ans