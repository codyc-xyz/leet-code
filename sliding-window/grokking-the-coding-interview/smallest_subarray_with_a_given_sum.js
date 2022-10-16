// Given an array of positive numbers and a positive number 'S', find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0, if no such subarray exists (EASY)

function find_smallest_subarray_with_given_sum(S, arr) {
  let windowSum = 0
  let windowStart = 0
  let minLength = Math.pow(10, 1000)
  let subArray = []
  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    windowSum += arr[windowEnd];
    subArray += arr[windowEnd]
    while (windowSum >= S) {
      minLength = math.Min(subArray.length, minLength)
      windowSum -= arr[windowStart]
      subArray -= arr[windowStart]
      windowStart += 1
    }
  }
  return minLength == Math.pow(10, 1000) ? 0 : minLength
}