# You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. 
# You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

# A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. 
# More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

# Return the number of weak characters.

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        ans = 0
        hm = {}
        stack = []
        for i, n in enumerate(properties):
            stack.append([n[0], n[1]])
        
        for p in properties:
            for s in stack:
                if p[0] < s[0] and p[1] < s[1]:
                    ans += 1
                    break
        return ans
                    