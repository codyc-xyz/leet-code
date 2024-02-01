# Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        ans = []
        ans.append(["Table"])
        food = orders
        food.sort(key=lambda x: x[2])
        seenFood = set()
        foodKey ={}
        for _,_,f in food:
            if f not in seenFood:
                ans[0].append(f)
                seenFood.add(f)
                foodKey[f] = len(ans[0]) - 1

        table = orders
        table.sort(key=lambda x: int(x[1]))
        seenTable = set()
        tableKey = {}
        for _,t,_ in table:
            if t not in seenTable:
                ans.append([t])
                seenTable.add(t)
                tableKey[t] = len(ans) - 1
        
        for j in range(1, len(ans)):
            for i in range(len(seenFood)):
                ans[j].append("0")

        for _, t, f in orders:
            currVal = int(ans[tableKey[t]][foodKey[f]]) + 1
            ans[tableKey[t]][foodKey[f]] = str(currVal)

        return ans
