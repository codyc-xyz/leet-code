# Design a food rating system that can do the following:

# Modify the rating of a food item listed in the system.
# Return the highest-rated food item for a type of cuisine in the system.
# Implement the FoodRatings class:
# FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
# foods[i] is the name of the ith food,
# cuisines[i] is the type of cuisine of the ith food, and
 #ratings[i] is the initial rating of the ith food.
# void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
# String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
# Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.hm = { c: [] for c in cuisines}
        self.foodRatings = {}
        for f, c in zip(foods, cuisines):
            self.hm[c].append(f)
        self.foodGroups = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings):
            heapq.heappush(self.foodGroups[c], [-r, f])
            self.foodRatings[f] = -r

    def changeRating(self, food: str, newRating: int) -> None:
        for c in self.hm:
            if food in self.hm[c]:
                heapq.heappush(self.foodGroups[c], [-newRating, food])
                self.foodRatings[food] = -newRating
                break
       
    def highestRated(self, cuisine: str) -> str:
        while self.foodGroups[cuisine][0][0] != self.foodRatings[self.foodGroups[cuisine][0][1]]:
            heapq.heappop(self.foodGroups[cuisine])
        return self.foodGroups[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)