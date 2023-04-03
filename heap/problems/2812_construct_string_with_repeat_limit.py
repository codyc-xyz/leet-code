# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

# Return the lexicographically largest repeatLimitedString possible.

# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        count = collections.Counter(s)
        heap = []
        for c in count:
            heapq.heappush(heap, [(ord('a') - ord(c)), -count[c], c])

        ans = ""
        repetitions = 0
        while heap:
            lexi, cnt, char = heapq.heappop(heap)
            if (not ans or char != ans[-1]) and cnt < 0:
                ans += char
                repetitions = 1
                if cnt < -1:
                    heapq.heappush(heap, [lexi, cnt + 1, char])
            elif ans and char == ans[-1] and repetitions < repeatLimit and cnt < 0:
                ans += char
                repetitions += 1
                heapq.heappush(heap, [lexi, cnt + 1, char])
            elif ans and char == ans[-1] and repetitions >= repeatLimit:
                if heap and heap[0][1] < 0:
                    lexi1, cnt1, char1 = heapq.heappop(heap)
                    ans += char1
                    repetitions = 1
                    heapq.heappush(heap, [lexi, cnt, char])
                    if cnt1 < -1:
                        heapq.heappush(heap, [lexi1, cnt1 + 1, char1])
                else:
                    return ans
            
        return ans