# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        res = [[0, 0] for _ in range(n)]

        for truster, trustee in trust:
            res[trustee - 1][1] += 1
            res[truster - 1][0] += 1

        for i, (trusting, trusted) in enumerate(res):
            if trusting == 0 and trusted == n - 1:
                return i + 1
        return -1