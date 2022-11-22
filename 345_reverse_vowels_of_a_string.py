# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        dq = deque()
        k = 0
        a = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                dq.appendleft(s[i])
                k += 1
        for i in range(len(s)):
            if s[i] in vowels:
                a[i] = dq.popleft()
        return "".join(a)
            