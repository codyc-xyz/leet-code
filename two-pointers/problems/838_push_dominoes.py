# There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
# After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# You are given a string dominoes representing the initial state where:
# dominoes[i] = 'L', if the ith domino has been pushed to the left,
# dominoes[i] = 'R', if the ith domino has been pushed to the right, and
# dominoes[i] = '.', if the ith domino has not been pushed.

# Return a string representing the final state.

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        queue = deque()
        for i, d in enumerate(dom):
            if d != '.':
                queue.append((i, d))
        
        while queue:
            i, d = queue.popleft()
            
            if d == 'R':
                if i + 1 < len(dom) and dom[i + 1] == '.':
                    if i + 2 < len(dom) and dom[i + 2] and dom[i + 2] == 'L':
                        queue.popleft()
                        continue
                    else:
                        dom[i + 1] = 'R'
                        queue.append((i + 1, 'R'))
            elif d == 'L':
                if i > 0 and dom[i - 1] == '.':
                    dom[i - 1] = 'L'
                    queue.append((i - 1, 'L'))
        return "".join(dom)