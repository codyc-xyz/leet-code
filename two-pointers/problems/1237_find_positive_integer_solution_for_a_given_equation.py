# Given a callable function f(x, y) with a hidden formula and a value z, reverse engineer the formula and return all positive integer pairs x and y where f(x,y) == z. 
# You may return the pairs in any order.

# While the exact formula is hidden, the function is monotonically increasing, i.e.:

# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        x, y, res = 1, 1000, []
        
        while y >= 1 and x <= 1000:
            if customfunction.f(x, y) > z:
                y -= 1
            elif customfunction.f(x, y) < z:
                x += 1
            else:
                res.append([x, y])
                x += 1
                y -= 1
        return res