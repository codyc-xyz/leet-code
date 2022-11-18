# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place return the new length of the array.

def remove_duplicates(arr):

  nextNonDup = 1
  for next in range(1, len(arr)):
    if arr[nextNonDup - 1] != arr[next]:
      arr[nextNonDup] = arr[next]
      nextNonDup += 1
  return nextNonDup

