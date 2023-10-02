# There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

# Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

# Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
# Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
# Alice and Bob cannot remove pieces from the edge of the line.
# If a player cannot make a move on their turn, that player loses and the other player wins.
# Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        consecAs, consecBs = [0], [0]
        for c in colors:
            if c == 'A':
                consecAs.append(consecAs[-1] + 1)
                consecBs.append(0)
            else:
                consecBs.append(consecBs[-1] + 1)
                consecAs.append(0)
        i = sumAs = sumBs = 0

        while i < len(colors):
            while i < len(colors) and consecAs[i + 1] == consecAs[i] + 1:
                i += 1
            if consecAs[i] > 2:
                sumAs += consecAs[i] - 2
            while i < len(colors) and consecBs[i + 1] == consecBs[i] + 1:
                i += 1
            if consecBs[i] > 2:
                sumBs += consecBs[i] - 2

        if sumAs > 0 or sumBs > 0:
            return sumAs > sumBs
        return False
