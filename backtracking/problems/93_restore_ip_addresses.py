#A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
# You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        ans = []

        def backtrack(curr, res, i):
            if i == len(s) and len(res) == 4:
                for r in res:
                    if len(r) > 1 and r[0] == '0':
                        return
                ip = ".".join(res)
                if len(ip) == len(s) + 3:
                    ans.append(ip)
                return
            elif i >= len(s):
                return
            
            if curr != "":
                if int(curr + s[i]) < 0 or int(curr + s[i]) > 255:
                    return
            curr += s[i]
            tmp = curr
            res.append(curr)
            curr = ""
            backtrack(curr, res, i + 1)
            res.pop()
            backtrack(tmp, res, i + 1)

        backtrack("", [], 0)
        return ans
