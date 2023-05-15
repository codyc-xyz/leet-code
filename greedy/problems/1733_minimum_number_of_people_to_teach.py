# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        ans = float('inf')
        seen = set()
        res = set()
        for a, b in friendships:
            for l in languages[a - 1]:
                if l in languages[b - 1]:
                    seen.add((a, b))
                    break
            if (a, b) not in seen:
                res.add((a, b))

        for i in range(1, n + 1):
            currAns = 0
            taught = set()
            for r in res:
                a, b = r
                if i not in languages[a - 1] and (a, i) not in taught:
                    currAns += 1
                    taught.add((a, i))
                if i not in languages[b - 1] and (b, i) not in taught:
                    currAns += 1
                    taught.add((b, i))

            ans = min(currAns, ans)
        return ans

