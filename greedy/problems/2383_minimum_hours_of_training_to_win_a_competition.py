# You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.

# You are also given two 0-indexed integer arrays energy and experience, both of length n.

# You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.

# Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].

# Before starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.

# Return the minimum number of training hours required to defeat all n opponents.

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        if sum(energy) >= initialEnergy:
            ans = sum(energy) + 1 - initialEnergy 
        else:
            ans = 0
        for energ, exp in zip(energy, experience):
            if initialExperience > exp:
                initialExperience += exp
            else:
                currExp = exp + 1 - initialExperience
                ans += currExp
                initialExperience += currExp + exp
        return ans
