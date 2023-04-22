# You are given two strings current and correct representing two 24-hour times.

# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

# In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.

# Return the minimum number of operations needed to convert current to correct.

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        ops = 0
        currMin = corrMin = ops = 0
        
    
        for i in range(len(current)):
            if i == 0:
                currMin += 600 * int(current[i])
                corrMin += 600 * int(correct[i])
            elif i == 1:
                currMin += 60 * int(current[i])
                corrMin += 60 * int(correct[i])
            elif i == 2:
                continue
            elif i == 3:
                currMin += 10 * int(current[i])
                corrMin += 10 * int(correct[i])
            elif i == 4:
                currMin += int(current[i])
                corrMin += int(correct[i])

        while corrMin >= currMin + 600:
            currMin += 600
            ops += 10

        while corrMin >= currMin + 60:
            currMin += 60
            ops += 1
        
        while corrMin >= currMin + 15:
            currMin += 15
            ops += 1
        
        while corrMin >= currMin + 5:
            currMin += 5
            ops += 1

        while corrMin >= currMin + 1:
            currMin += 1
            ops += 1

        return ops

        


            
                

               
