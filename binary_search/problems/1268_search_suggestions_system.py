# You are given an array of strings products and a string searchWord.

# Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

# Return a list of lists of the suggested products after each character of searchWord is typed.

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        curr = ""
        for s in searchWord:
            curr += s
            end = len(curr)
            start = -1
            l, r = 0, len(products) - 1
            while l <= r:
                m = (l + r) // 2
                if products[m][:end] == curr:
                    start = m
                if products[m][:end] >= curr:
                    r = m - 1
                else:
                    l = m + 1
            
            if start != -1:
                j = start
                while j < len(products) and products[j][:end] == curr and start + 3 > j:
                    j += 1
                ans.append(products[start:j])
            else:
                ans.append([])
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        for i in range(len(searchWord)):
            ans.append(self.searchResults(list(products), searchWord[:i + 1]))
        return ans
    def searchResults(self, products, pfix):
        res = []
        l = self.binSearch(products, pfix, True)
        r = self.binSearch(products, pfix, False)
        while l <= r and len(res) < 3 and products[l][:len(pfix)] == pfix:
            res.append(products[l])
            l += 1
        return res

    def binSearch(self, products, pfix, leftBias):
        l, r = 0, len(products) - 1
        while l < r:
            m = (l + r) // 2
            res = products[m][:len(pfix)]

            if res < pfix:
                l = m + 1
            elif res > pfix:
                r = m 
            else:
                if leftBias:
                    r = m 
                else:
                    l = m + 1
        return r if leftBias else l