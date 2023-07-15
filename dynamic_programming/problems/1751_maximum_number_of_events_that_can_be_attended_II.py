# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is , you cannot attend two events where one of them starts and the other ends on the same day.

# Return the maximum sum of values that you can receive by attending events.

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        N = len(events)
        events.sort()
        dp = [[-1] * N for _ in range(k + 1)]
        starts = [start for start, end, value in events]

        def dfs(cur_idx, count):
            if count == 0 or cur_idx == N:
                return 0
            if dp[count][cur_idx] != -1:
                return dp[count][cur_idx]

            next_idx = bisect_right(starts, events[cur_idx][1])
            dp[count][cur_idx] = max(
                dfs(cur_idx + 1, count), events[cur_idx][2] + dfs(next_idx, count - 1))
            return dp[count][cur_idx]
        return dfs(0, k)
