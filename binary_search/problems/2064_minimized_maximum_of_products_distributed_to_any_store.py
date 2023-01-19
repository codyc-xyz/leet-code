# You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

# You need to distribute all products to the retail stores following these rules:
# A store can only be given at most one product type but can be given any amount of it.
# After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

# Return the minimum possible x.

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def minMax(m):
            stores = n
            for q in quantities:
                stores -= math.ceil(q / m)
            return stores
                
        l, r = 1, max(quantities)
        while l < r:
            m = (l + r) // 2
            
            if minMax(m) < 0:
                l = m + 1
            else:
                r = m
        return l