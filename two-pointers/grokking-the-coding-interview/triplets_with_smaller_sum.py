# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
# Write a function to return the count of such triplets.

def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0
  for i in range(len(arr) - 2):
    count += search_pair(arr, target - arr[i], i)
  return count

def search_pair(arr, target_sum, first):
  count = 0
  left, right = first + 1, len(arr) - 1
  while(left < right):
    if arr[left] + arr[right] < target_sum:
      count += right - left
      left += 1
    else:
      right -= 1
  return count