# The factorial of a positive integer n is the product of all positive integers less than or equal to n.

# For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

# We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply '*', divide '/', add '+', and subtract '-' in this order.
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.

# However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

# Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.

# Given an integer n, return the clumsy factorial of n.

class Solution:
    def clumsy(self, n: int) -> int:
        stack = deque()
        i = 0
        while n > 0:
           
            if not stack:
                stack.append(n)
                n -= 1
                continue
            elif stack and i == 0:
                stack[-1] *= n
            elif i == 1:
                stack[-1] //= n
            elif i == 2:
                stack[-1] += n
            elif i == 3:
                if n > 2:
                    stack[-1] -= ((n * (n - 1)) // (n - 2))
                    i = 2
                    n -= 3
                    continue
                elif n == 2:
                    stack[-1] -= (n * (n - 1))
                    break
                elif n == 1:
                    stack[-1] -= n
                    break
            i += 1
            if i == 4:
                i = 0
            n -= 1
            
        return stack[-1]