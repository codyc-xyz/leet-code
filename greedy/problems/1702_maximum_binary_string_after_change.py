# You are given a binary string binary consisting of only 0's or 1's. You can apply each of the following operations any number of times:

# Operation 1: If the number contains the substring "00", you can replace it with "10".
# For example, "00010" -> "10010"
# Operation 2: If the number contains the substring "10", you can replace it with "01".
# For example, "00010" -> "00001"
# Return the maximum binary string you can obtain after any number of operations. Binary string x is greater than binary string y if x's decimal representation is greater than y's decimal representation.

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if '0' not in binary:
            return binary
        idx = binary.index('0')
        ans = ""
        for i in range(idx):
            ans += '1'

        zeros = 0
        for i in range(idx, len(binary)):
            if binary[i] == '0':
                zeros += 1

        while zeros >= 2:
            ans += '1'
            zeros -= 1
        ans += '0'
        while len(ans) < len(binary):
            ans += '1'
        return ans
