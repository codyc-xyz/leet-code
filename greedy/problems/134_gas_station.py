# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasCost = []
        costSum = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            gasCost.append([g - c, i])
            costSum += gasCost[-1][0]

        if costSum < 0:
            return -1
    
        for c, i in gasCost:
            if c >= 0:
                j = i + 1
                rollingCost = c
                while j != i:
                    if j == len(gasCost):
                        if i == 0:
                            break
                        j = 0
                    rollingCost += gasCost[j][0]
                    if rollingCost < 0:
                        break
                    j += 1
                if rollingCost >= 0:
                    return i
        return -1


        

        
