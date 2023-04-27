# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        count = collections.Counter(tasks)
        rounds = 0
        for c in count:
            curr = count[c]
            if curr == 1:
                return -1
            if curr - 3 >= 2:
                div, mod = divmod(curr, 3)
                curr = mod
                rounds += div
                if not curr:
                    continue
            if curr == 4:
                rounds += 2
            else:
                rounds += 1
        return rounds
