# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        seen = set()

        for w, l in matches:
            if l in losses:
                losses[l] += 1
            else:
                losses[l] = 1
            seen.add(w)
            seen.add(l)

        ans = [[], []]
        for p in seen:
            if p not in losses:
                ans[0].append(p)
            elif losses[p] == 1:
                ans[1].append(p)

        return [sorted(ans[0]), sorted(ans[1])]
