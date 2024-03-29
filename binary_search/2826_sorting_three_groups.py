# You are given a 0-indexed integer array nums of length n.

# The numbers from 0 to n - 1 are divided into three groups numbered from 1 to 3, where number i belongs to group nums[i]. Notice that some groups may be empty.

# You are allowed to perform this operation any number of times:

# Pick number x and change its group. More formally, change nums[x] to any number from 1 to 3.
# A new array res is constructed using the following procedure:

# Sort the numbers in each group independently.
# Append the elements of groups 1, 2, and 3 to res in this order.
# Array nums is called a beautiful array if the constructed array res is sorted in non-decreasing order.

# Return the minimum number of operations to make nums a beautiful array.

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        arr = []
        def binSearch(arr, target):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            return l

        for i in range(N):
            pos = binSearch(arr, nums[i])
            if pos == len(arr):
                arr.append(nums[i])
            else:
                arr[pos] = nums[i]
        return N - len(arr)