# Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

# Implement the MagicDictionary class:

# MagicDictionary() Initializes the object.
# void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
# bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.

class MagicDictionary:

    def __init__(self):
        self.magicDict = []
        

    def buildDict(self, dictionary: List[str]) -> None:
        self.magicDict = dictionary

    def search(self, searchWord: str) -> bool:
        for d in self.magicDict:
            diff = 0
            i = 0
            if abs(len(searchWord) - len(d)) > 0:
                continue
            for c in d:
                if c != searchWord[i]:
                    diff += 1
                    if diff > 1:
                        break
                i += 1
            if diff == 1:
                return True
        return False


        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)