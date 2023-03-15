#A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
# You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ans = []

        if len(s) > 12:
            return ans

        def backtrack(i, dots, currIp):
            if dots == 4 and i == len(s):
                ans.append(currIp[:-1])
                return
            if dots > 4 or i >= len(s):
                return
            
            for j in range(i, min(i + 3, len(s))):
                curr = s[i:j + 1]
                if int(curr) < 256 and (i == j or s[i] != '0'):
                    backtrack(j + 1, dots + 1, currIp + curr + '.')
        backtrack(0, 0, "")
        return ans
