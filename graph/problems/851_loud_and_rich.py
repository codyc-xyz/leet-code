# There is a group of n people labeled from 0 to n - 1 where each person has a different amount of money and a different level of quietness.

# You are given an array richer where richer[i] = [ai, bi] indicates that ai has more money than bi and an integer array quiet where quiet[i] is the quietness of the ith person. All the given data in richer are logically correct (i.e., the data will not lead you to a situation where x is richer than y and y is richer than x at the same time).

# Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]) among all people who definitely have equal to or more money than the person x.

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        richerThan = defaultdict(list)
        for richerP, poorerP in richer:
            richerThan[poorerP].append(richerP)

        def dfs(p):
            for richerP in richerThan[p]:
                if quiet[richerP] < self.minLoud:
                    self.minLoud = quiet[richerP]
                    self.loudestP = richerP
                dfs(richerP)

        ans = []

        for i in range(len(quiet)):
            self.minLoud = quiet[i]
            self.loudestP = i
            dfs(i)
            ans.append(self.loudestP)
        return ans




