# There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

# You have to form a team of 3 soldiers amongst them under the following rules:

# Choose 3 soldiers with index(i, j, k) with rating(rating[i], rating[j], rating[k]).
# A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where(0 <= i < j < k < n).
# Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

class Solution:
    def numTeams(self, rating: List[int]) -> int:

        def backtrack(i, numSoldiers, prev, bias):
            res = 0

            if numSoldiers == 3:
                return 1
            if i == len(rating):
                return 0
            if bias:
                if rating[i] < prev:
                    res += backtrack(i + 1, numSoldiers+1, rating[i], bias)
                res += backtrack(i+1, numSoldiers, prev, bias)
            elif not bias:
                if rating[i] > prev:
                    res += backtrack(i+1, numSoldiers+1, rating[i], bias)
                res += backtrack(i+1, numSoldiers, prev, bias)
            return res

        return backtrack(0, 0, float('inf'), True) + backtrack(0, 0, 0, False)


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        greaterR = [0 for _ in range(N)]
        lessR = [0 for _ in range(N)]
        greaterL = [0 for _ in range(N)]
        lessL = [0 for _ in range(N)]

        for i in range(N - 1):
            for j in range(i+1, N):
                if rating[j] > rating[i]:
                    greaterR[i] += 1
                else:
                    lessR[i] += 1

        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                if rating[j] > rating[i]:
                    greaterL[i] += 1
                else:
                    lessL[i] += 1
        ans = 0
        for i in range(N):
            ans += lessL[i] * greaterR[i] + greaterL[i] * lessR[i]
        return ans
