# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. 
# All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.

# Otherwise, they will leave it and go to the queue's end.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack 
# (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). 
# Return the number of students that are unable to eat.

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = deque(students)
        sandwiches = deque(sandwiches)
        k = collections.Counter(students)
        while sandwiches and stack and k[0] > 0 and k[1] > 0:
            while sandwiches and stack and sandwiches[0] == stack[0]:
                k[stack[0]] -= 1
                stack.popleft()
                sandwiches.popleft()
            if stack:
                stack.append(stack.popleft())
        return len(stack)