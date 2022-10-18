// Given a string with lowercase letters only, if you are allowed to replace no more than 'k' letters with any letter, find the length of the longest substring having the same letters after replacement

function longest_substring_with_same_letters_after_replacement(string, K) {
  let arr = string.split('')
  let windowStart = 0
  let substring = []
  let maxRepeatLetterCount = 0
  for(let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
    while(arr[windowEnd] === arr[windowEnd + 1]) {
      substring += arr[windowEnd]
      windowEnd += 1
    }
    maxRepeatLetterCount = Math.max(maxRepeatLetterCount, substring.length + 1)
    substring -= arr[windowStart]
    windowStart += 1
  }
  return maxRepeatLetterCount
}