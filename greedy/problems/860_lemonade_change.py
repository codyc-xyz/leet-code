# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        leftOver = [0, 0, 0]

        for b in bills:
            if b == 5:
                leftOver[0] += 1
            elif b == 10:
                if not leftOver[0]:
                    return False
                else:
                    leftOver[0] -= 1
                    leftOver[1] += 1
            else:
                if not leftOver[0] or not leftOver[1] and leftOver[0] < 3:
                    return False
                else:
                    if leftOver[1]:
                        leftOver[1] -= 1
                        leftOver[0] -= 1
                    elif not leftOver[1]:
                        leftOver[0] -= 3
                    leftOver[2] += 1
        return True