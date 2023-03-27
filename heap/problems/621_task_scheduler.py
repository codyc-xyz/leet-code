# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = collections.Counter(tasks)

        arr = []
        for c in count:
            arr.append(count[c] * -1)
        time = 0
        arr.sort()
        while arr[0] < 0:
            arr[0] += 1
            time += 1
            k = n 
            for i in range(1, len(arr)):
                if k == 0:
                    break
                if arr[i] < 0:
                    arr[i] += 1
                    time += 1
                    k -= 1
            arr.sort()
            if arr[0] < 0:
                time += k 
        return time
