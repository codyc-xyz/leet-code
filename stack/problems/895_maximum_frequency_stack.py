# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

class FreqStack:

    
    def __init__(self):
        self.stack = []
        self.hm = {}

    def push(self, val: int) -> None:
        if val in self.hm:
            self.hm[val] += 1
        else:
            self.hm[val] = 1
        self.stack.append([val, self.hm[val]])
        
    def pop(self) -> int:
        freq = max(self.hm.values())
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][1] == freq:
                self.hm[self.stack[i][0]] -= 1
                if self.hm[self.stack[i][0]] < 1:
                    del self.hm[self.stack[i][0]]
                return self.stack.pop(i)[0]