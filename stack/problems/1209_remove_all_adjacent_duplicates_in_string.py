# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                if stack[-1][1] + 1 == k:
                    K = k - 1
                    while K:
                        stack.pop()
                        K -= 1
                    continue
                else:
                    stack.append([c, stack[-1][1] + 1])
            else:
                stack.append([c, 1])
        ans = [stack[i][0] for i in range(len(stack))]
        return "".join(ans)