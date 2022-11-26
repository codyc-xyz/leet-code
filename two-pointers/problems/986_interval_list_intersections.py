# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
# Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        first = second = 0
        output = []
        length = max(len(firstList), len(secondList))
        while first < len(firstList) and second < len(secondList):
            if firstList[first][0] <= secondList[second][1] and firstList[first][1] >= secondList[second][0]:
                output.append([max(firstList[first][0], secondList[second][0]), min(firstList[first][1], secondList[second][1])])
            
            if firstList[first][1] > secondList[second][1]:
                second += 1
            else:
                first += 1
        return output