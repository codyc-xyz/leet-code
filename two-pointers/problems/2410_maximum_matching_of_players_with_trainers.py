# You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. 
# You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

# The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. 
# Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

# Return the maximum number of matchings between players and trainers that satisfy these conditions.

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        match = 0
        player = len(players) - 1
        trainer = len(trainers) - 1
        
        while player >= 0 and trainer >= 0:
            if trainers[trainer] >= players[player]:
                match += 1
                player -= 1
                trainer -= 1
            else:
                player -= 1
        return match