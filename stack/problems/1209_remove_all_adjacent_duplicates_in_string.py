# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        ans = ""
        for c in s:
            if stack and c == stack[-1][0]:
                stack.append([c, stack[-1][1] + 1])
            else:
                stack.append([c, 1])
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()
            
        while stack:
            ans += stack.popleft()[0]
        return ans