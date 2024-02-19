# You are given a 2D 0-indexed array of strings, access_times, with size n. For each i where 0 <= i <= n - 1, access_times[i][0] represents the name of an employee, and access_times[i][1] represents the access time of that employee. All entries in access_times are within the same day.

# The access time is represented as four digits using a 24-hour time format, for example, "0800" or "2250".

# An employee is said to be high-access if he has accessed the system three or more times within a one-hour period.

# Times with exactly one hour of difference are not considered part of the same one-hour period. For example, "0815" and "0915" are not part of the same one-hour period.

# Access times at the start and end of the day are not counted within the same one-hour period. For example, "0005" and "2350" are not part of the same one-hour period.

# Return a list that contains the names of high-access employees with any order you want.

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        
        accesses = defaultdict(list)
        access_times.sort(key=lambda x: int(x[1]))

        for p, a in access_times:
            accesses[p].append(int(a))
        ans = []
        for a in accesses:
            i = 0
            while i < len(accesses[a]) - 2:
                if accesses[a][i+2] - accesses[a][i] < 100:
                    ans.append(a)
                    break
                i += 1
        return ans

