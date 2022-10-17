// Given a string, find the length of the longest substring in it with no more than K distinct characters

function find_largest_substring_with_K_distinct_characters(K, string) {
  let arr = string.split('')
  let substring = []
  let largestLength = 0
  let windowStart = 0
  for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    while (substring.uniq <= K) {
      substring += arr[windowEnd]
    }
      largestLength = math.Max(largestSubstring.length, substring.length)
      substring -= arr[windowStart]
      windowStart += 1
  }
  return largestLength
}