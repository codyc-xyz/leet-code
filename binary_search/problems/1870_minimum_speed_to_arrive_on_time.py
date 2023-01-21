# You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

# Each train can only depart at an integer hour, so you may need to wait in between each train ride.

# For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 > hour:
            return -1
        l, r = 1, 10**7
        best_time = hour
        ans = -1
        while l <= r:
            m = (l + r) // 2
            res = 0
            for i, d in enumerate(dist):
                if i != len(dist) - 1:
                    res += math.ceil(d / m)
                else:
                    res += d / m
            diff = abs(res - hour)
            if diff < best_time and res <= hour:
                best_time = diff
                ans = m
            if res - hour <= 0:
                r = m - 1
            else:
                l = m + 1

        return int(ans)