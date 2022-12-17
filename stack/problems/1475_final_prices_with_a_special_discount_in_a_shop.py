# You are given an integer array prices where prices[i] is the price of the ith item in a shop.

# There is a special discount for items in the shop. 
# If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. 
# Otherwise, you will not receive any discount at all.

# Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(prices) - 1):
            j = i + 1
            flag = False
            while j < len(prices):
                if prices[j] <= prices[i]:
                    flag = True
                    break
                else:
                    j += 1
            if flag == True:
                ans.append(prices[i] - prices[j])
            else:
                ans.append(prices[i])
        ans.append(prices[i + 1])
        return ans