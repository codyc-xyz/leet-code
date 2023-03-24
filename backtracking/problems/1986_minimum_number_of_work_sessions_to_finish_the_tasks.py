# There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. 
# A work session is when you work for at most sessionTime consecutive hours and then take a break.

# You should finish the given tasks in a way that satisfies the following conditions:

# If you start a task in a work session, you must complete it in the same work session.
# You can start a new task immediately after finishing the previous one.
# You may complete the tasks in any order.
# Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

# The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse = True)

        def completeTasks(i):
            if i == len(tasks):
                return True
            
            for j in range(self.m):
                if timeRemaining[j] >= tasks[i]:
                    timeRemaining[j] -= tasks[i]
                    if completeTasks(i + 1):
                        return True
                    timeRemaining[j] += tasks[i]
                    if timeRemaining[j] == tasks[i]:
                        break
            return False

        l, r = 1, len(tasks)
        while l < r:
            self.m = (l + r) // 2
            timeRemaining = [sessionTime] * self.m
            if completeTasks(0):
                r = self.m
            else:
                l = self.m + 1      
        return l
            