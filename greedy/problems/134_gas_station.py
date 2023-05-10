# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasCost = []
        for g, c in zip(gas, cost):
            gasCost.append(g - c)
 
        if sum(gasCost) < 0:
            return -1
        currSum = 0
        idx = 0
        for i in range(len(gasCost)):
            currSum += gasCost[i]
            if currSum < 0:
                currSum, idx = 0, i + 1
        return idx