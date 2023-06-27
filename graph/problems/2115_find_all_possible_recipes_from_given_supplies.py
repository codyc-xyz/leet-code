# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

# Return a list of all the recipes that you can create. You may return the answer in any order.

# Note that two recipes may contain each other in their ingredients.

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        supplies = set(supplies)
        ans = []
        newRecipe = True
        seen = set()
        while newRecipe:
            newRecipe = False
            for i in range(len(recipes)):
                if i in seen:
                    continue
                if all(j in supplies for j in ingredients[i]):
                    ans.append(recipes[i])
                    supplies.add(recipes[i])
                    seen.add(i)
                    newRecipe = True

        return ans
