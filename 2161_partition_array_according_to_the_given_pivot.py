# You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
  # Every element less than pivot appears before every element greater than pivot.
  # Every element equal to pivot appears in between the elements less than and greater than pivot.
  # The relative order of the elements less than pivot and the elements greater than pivot is maintained.
    # More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. 
    # For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. 
    # Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.

# Return nums after the rearrangement.

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = 0, len(nums) - 1
        less = deque()
        more = deque()
        k = 0
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                more.append(nums[i])
            else:
                k += 1
        while less:
            nums[left] = less.popleft()
            left += 1
        while more:
            nums[right] = more.pop()
            right -= 1
        while k > 0:
            nums[left] = pivot
            left += 1
            k -= 1
        return nums