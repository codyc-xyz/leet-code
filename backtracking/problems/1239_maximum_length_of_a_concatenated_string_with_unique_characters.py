# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def maxLength(self, arr: List[str]) -> int:

        self.maxLen = 0
        seenChars = defaultdict(int)
        def backtrack(curr, i, seenChars):
            if i == len(arr):
                flag = False
                for c in seenChars:
                    if seenChars[c] > 1:
                        flag = True
                        break
                if flag == False:
                    self.maxLen = max(self.maxLen, len("".join(curr))) 
                return

            for c in arr[i]:
                seenChars[c] += 1
            curr.append(arr[i])
            backtrack(curr, i + 1, seenChars)
            curr.pop()
            for c in arr[i]:
                seenChars[c] -= 1
            backtrack(curr, i + 1, seenChars)
        backtrack([], 0, seenChars)
        return self.maxLen
    
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        def backtrack(i, currSet):
            if i == len(arr):
                self.ans = max(len(currSet), self.ans)
                return
            backtrack(i+1, currSet)
            add = True
            tempSet = set()
            for c in arr[i]:
                if c in currSet or c in tempSet:
                    add = False
                    break
                tempSet.add(c)
            if add:
                newSet = currSet | tempSet
                backtrack(i + 1, newSet)
        backtrack(0, set())
        return self.ans
