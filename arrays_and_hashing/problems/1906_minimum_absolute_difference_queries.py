# The minimum absolute difference of an array a is defined as the minimum value of |a[i] - a[j]|, where 0 <= i < j < a.length and a[i] != a[j]. If all elements of a are the same, the minimum absolute difference is -1.

# For example, the minimum absolute difference of the array [5,2,3,7,2] is |2 - 3| = 1. Note that it is not 0 because a[i] and a[j] must be different.
# You are given an integer array nums and the array queries where queries[i] = [li, ri]. For each query i, compute the minimum absolute difference of the subarray nums[li...ri] containing the elements of nums between the 0-based indices li and ri (inclusive).

# Return an array ans where ans[i] is the answer to the ith query.

# A subarray is a contiguous sequence of elements in an array.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.

class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        minDiff = defaultdict(list)
        ans = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    minDiff[i].append(float('inf'))
                else:
                    minDiff[i].append(abs(nums[i] - nums[j]))
                
            
        for a, b in queries:
            currMin = float('inf')
            for i in range(a, b):
                currMin = min(currMin, min(minDiff[i][:b-i]))
            ans.append(currMin) if currMin != float('inf') else ans.append(-1)
        return ans
        
class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        res = [[0 for _ in range(101)] for _ in range(N+1)]
        ans = []

        for i in range(1, N + 1):
            for j in range(101):
                res[i][j] = res[i-1][j] + (1 if nums[i-1] == j else 0)

        for a, b in queries:
            prev = -1
            currMin = float('inf')
            for i in range(101):
                if res[b+1][i] - res[a][i] > 0:
                    if prev != -1:
                        currMin = min(currMin, i-prev)
                    prev = i
            ans.append(currMin) if currMin != float('inf') else ans.append(-1)
        return ans

                


        

