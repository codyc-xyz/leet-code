# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        buckets = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heapq.heapify(buckets)
        ans = ""
        while buckets[0][0] < 0:
            if len(ans) < 2 or (ans[-1] != buckets[0][1] or ans[-2] != buckets[0][1]) and buckets[0][0] < 0:
                num, char = heapq.heappop(buckets)
                ans += char
                heapq.heappush(buckets, [num + 1, char])
            elif len(ans) > 1 and ans[-1] == buckets[0][1] and ans[-2] == buckets[0][1]:
                if buckets[1][0] < 0:
                    buckets[1][0] += 1
                    ans += buckets[1][1]
                elif buckets[2][0] < 0:
                    buckets[2][0] += 1
                    ans += buckets[2][1]
                else:
                    break
            else:
                break

        return ans


