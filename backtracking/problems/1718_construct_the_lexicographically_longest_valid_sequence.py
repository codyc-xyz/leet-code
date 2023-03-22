# Given an integer n, find a sequence that satisfies all of the following:

# The integer 1 occurs once in the sequence.
# Each integer between 2 and n occurs twice in the sequence.
# For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
# The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

# Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

# A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        self.maxAns = ans = [0] * (n * 2 - 1)
        used = set()
        def backtrack(i, ans, used):
            if len(used) == n:
                for i in range(len(ans)):
                    if ans[i] > self.maxAns[i]:
                        self.maxAns = ans[:]
                        break
                    elif ans[i] < self.maxAns[i]:
                        break
                return
            
            if ans[i] == 0:
                for j in range(n, 1, -1):
                    if j not in used and j + i < len(ans) and ans[j + i] == 0:
                        ans[i] = j
                        ans[i + j] = j
                        used.add(j)
                        backtrack(i + 1, ans, used)
                        used.remove(j)
                        ans[i] = 0
                        ans[i + j] = 0
                if 1 not in used:
                    used.add(1)
                    ans[i] = 1
                    backtrack(i + 1, ans, used)
                    used.remove(1)
                    ans[i] = 0
            else:
                backtrack(i + 1, ans, used)
           
        backtrack(0, ans, used)
        return self.maxAns
