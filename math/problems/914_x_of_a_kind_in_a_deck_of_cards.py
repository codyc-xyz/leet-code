# You are given an integer array deck where deck[i] represents the number written on the ith card.

# Partition the cards into one or more groups such that:

# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        numCards = len(set(deck))
        gcd = defaultdict(int)
        count = collections.Counter(deck)

        for c in count:
            for i in range(2, count[c] + 1):
                if not count[c] % i:
                    gcd[i] += 1
        return numCards in gcd.values()
