# You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

# Return the rearranged number with minimal value.

# Note that the sign of the number does not change after rearranging the digits.

class Solution:
    def smallestNumber(self, num: int) -> int:
        numArr = []
        neg = False
        for n in str(num):
            if n == '-':
                neg = True
                continue
            numArr.append(n)
    
        if not neg:
            numArr.sort()
            if numArr[0] == '0':
                i = 0
                while i < len(numArr) and numArr[i] == '0':
                    i += 1
                if i == len(numArr):
                    return 0
                numArr[0], numArr[i] = numArr[i], numArr[0]
        else:
            numArr.sort(reverse=True)

        ans = '' if not neg else '-'
        for n in numArr:
            ans += n
        return int(ans)
