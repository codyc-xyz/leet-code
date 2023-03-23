# You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

# Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

# 0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type), f.length >= 3, and f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
# Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

# Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        self.ans = []
        N = len(num)
        def backtrack(i, path, curr):
            if self.ans:
                return
            if len(path) > 2 and path[-1] != path[-2] + path[-3] or curr == '0' or path and path[-1] > 2147483647:
                return
            if i == len(num):
                self.flag = True
                if len(path) > 2:
                    self.flag = False
                    currLen = 0
                    for i in range(len(path) - 1, 1, -1):
                        if path[i] != path[i - 1] + path[i - 2]:
                            self.flag = True
                            break
                    for i in range(len(path)):
                        currLen += len(str(path[i]))
                if not self.flag and currLen == N:
                    self.ans = path
                return
            
            curr = curr + num[i]
            path.append(int(curr))
            backtrack(i + 1, path[:], "")
            path.pop()
            backtrack(i + 1, path[:], curr)
           

        backtrack(0, [], "")
        return self.ans