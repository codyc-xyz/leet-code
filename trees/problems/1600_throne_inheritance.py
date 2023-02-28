# A kingdom consists of a king, his children, his grandchildren, and so on. Every once in a while, someone in the family dies or a child is born.

# The kingdom has a well-defined order of inheritance that consists of the king as the first member. 
# Let's define the recursive function Successor(x, curOrder), which given a person x and the inheritance order so far, returns who should be the next person after x in the order of inheritance.

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.hm = {kingName : []}
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.hm[parentName].append(childName)
        self.hm[childName] = []
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(person):
            if person not in self.dead:
                order.append(person)
            if person in self.hm:
                for child in self.hm[person]:
                    dfs(child)
        dfs(self.king)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()