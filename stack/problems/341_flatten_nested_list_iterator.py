# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

# Your code will be tested with the following pseudocode:
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#    append iterator.next() to the end of res
# return res

# If res matches the expected flattened list, then your code will be judged as correct.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = deque(nestedList)
        
    def next(self) -> int:
        return self.stack.popleft()
        
    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[0].isInteger():
                return True
            top = self.stack.popleft()
            self.stack.extendleft(top.getList()[::-1])

        return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = []
        strList = str(nestedList)
        neg = False
        i = 0
        while i < len(strList):
            c = strList[i]
            j = i
            if c == '-':
                neg = True
            if c.isnumeric():
                res = ""
                while i < len(strList) and strList[j].isnumeric():
                    res += strList[j]
                    j += 1
                self.flattened.append(
                    int(res)) if not neg else self.flattened.append(int(res) * -1)
                neg = False
            i = max(j, i + 1)
        self.i = 0

    def next(self) -> int:
        ans = self.flattened[self.i]
        self.i += 1
        return ans

    def hasNext(self) -> bool:
        return self.i < len(self.flattened)
