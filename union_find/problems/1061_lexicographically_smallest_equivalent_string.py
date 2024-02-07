# You are given two strings of the same length s1 and s2 and a string baseStr.

# We say s1[i] and s2[i] are equivalent characters.

# For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:

# Reflexivity: 'a' == 'a'.
# Symmetry: 'a' == 'b' implies 'b' == 'a'.
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        equiv = defaultdict(set)
        smallest = defaultdict(str)
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            equiv[c1].add(c2)
            equiv[c2].add(c1)

        def setMinChar(curr, minCh):
            if curr in smallest:
                return
            smallest[curr] = minCh
            for eq in equiv[curr]:
                setMinChar(eq, minCh)

        for c in sorted(equiv.keys()):
            if c in smallest:
                continue
            setMinChar(c, c)
        return ''.join([smallest[c] if c in smallest else c for c in baseStr])
            
        

        
                    


