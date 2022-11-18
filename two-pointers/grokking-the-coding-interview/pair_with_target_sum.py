# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

def pair_with_target_sum(arr, target_sum):
  right, left = len(arr) - 1, 0
  currSum = 0

  while right > left:
    currSum = arr[right] + arr[left]

    if currSum = target_sum:
      return [left, right]    
    elif currSum > target_sum:
      right -= 1
    else:
      left += 1

  return [-1, -1] 
