# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        n1 = len(str(low))
        n2 = len(str(high))
        ans = []
        for i in range(1, 10):
            res = ""
            for j in range(i, 10):
                res += str(j)
                curr = int(res)
                if curr >= low and curr <= high:
                    ans.append(curr)
                if int(res) > high:
                    break
        return sorted(ans)