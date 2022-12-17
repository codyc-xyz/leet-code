# The Leetcode file system keeps a log each time some user performs a change folder operation.

# The Leetcode file system keeps a log each time some user performs a change folder operation.

# "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
# "./" : Remain in the same folder.
# "./" : Remain in the same folder.

# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.
# You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == '../': 
                if count > 0:
                    count -= 1
            elif log == './':
                continue
            else:
                count += 1
        return count