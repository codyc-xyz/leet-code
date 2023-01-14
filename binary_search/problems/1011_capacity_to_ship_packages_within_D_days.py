# A conveyor belt has packages that must be shipped from one port to another within days days.

# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
# We may not load more weight than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        l, r = 0, max(weights) * len(weights)
        ans = 0
        while l <= r:
            capacity = m = (l + r) // 2
            time = 1
            flag = True
            for i, w in enumerate(weights):
                if capacity > w:
                    capacity -= w
                elif capacity < w:
                    if w > m:
                        flag = False
                        break
                    capacity = m - w
                    time += 1
                else:
                    if i < len(weights) - 1:
                        capacity = m
                        time += 1
            if time <= days and flag == True:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans