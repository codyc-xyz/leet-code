# You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have been placed of type orderTypei at the price pricei. The orderTypei is:

# 0 if it is a batch of buy orders, or
# 1 if it is a batch of sell orders.
# Note that orders[i] represents a batch of amounti independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.

# There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:

# If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
# Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.
# Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo 109 + 7.

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        mod = 10**9 + 7
        buy = []
        sell = []

        for price, amount, orderType in orders:
            if orderType == 0:
                while sell and sell[0][0] <= price and amount > 0:
                    if sell[0][1] > amount:
                        sell[0][1] -= amount
                        amount = 0
                        break
                    elif sell[0][1] < amount:
                        amount -= sell[0][1]
                        heapq.heappop(sell)
                        continue
                    else:
                        heapq.heappop(sell)
                        amount = 0
                        break
                if amount > 0:
                    heapq.heappush(buy, [-price, amount])

            elif orderType == 1:
                while buy and -buy[0][0] >= price and amount > 0:
                    if buy[0][1] > amount:
                        buy[0][1] -= amount
                        amount = 0
                        break
                    elif buy[0][1] < amount:
                        amount -= buy[0][1]
                        heapq.heappop(buy)
                        continue
                    else:
                        heapq.heappop(buy)
                        amount = 0
                        break
                if amount > 0:
                    heapq.heappush(sell, [price, amount])
        
        totAmt = 0
        for price, amount in buy:
            totAmt += amount
        for price, amount in sell:
            totAmt += amount
        return totAmt % mod
