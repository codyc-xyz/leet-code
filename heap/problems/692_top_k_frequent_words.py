# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        count = dict(sorted(count.items(), key = lambda item: item[1], reverse=True))
        
        ans = []
        for c in count:
            ans.append(c)

            if len(ans) > 1 and count[ans[-2]] == count[ans[-1]]:
                j = len(ans) - 1
                while j > 0 and ans[j] < ans[j - 1] and count[ans[j]] == count[ans[j - 1]]:
                    ans[j - 1], ans[j] = ans[j], ans[j - 1]
                    j -= 1

        return ans[:k]
