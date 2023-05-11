# Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

# The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

# Any two characters may be swapped, even if they are not adjacent.

class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        count = collections.Counter(s)
        ones = count['1']
        zeros = count['0']
        if n % 2 and abs(ones - zeros) > 1:
            return -1
        elif not n % 2 and ones - zeros != 0:
            return -1

        if ones == zeros:
            ans1, ans2 = [], []

            for i in range(n):
                if i % 2:
                    ans1.append('0')
                    ans2.append('1')
                else:
                    ans1.append('1')
                    ans2.append('0')
            swaps1 = swaps2 = 0

            for i in range(n):
                if s[i] != ans1[i]:
                    swaps1 += 1
                else:
                    swaps2 += 1
            return math.ceil(min(swaps1, swaps2) / 2)
        elif ones > zeros:
            ans = []
            for i in range(n):
                if not i % 2:
                    ans.append('1')
                else:
                    ans.append('0')
            swaps = 0
            for i in range(n):
                if s[i] != ans[i]:
                    swaps += 1
            return math.ceil(swaps / 2)
        else:
            ans = []
            for i in range(n):
                if not i % 2:
                    ans.append('0')
                else:
                    ans.append('1')
            swaps = 0
            for i in range(n):
                if s[i] != ans[i]:
                    swaps += 1
            return math.ceil(swaps / 2)
      
      

