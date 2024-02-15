# A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign.

# For example, "$100", "$23", and "$6" represent prices while "100", "$", and "$1e5" do not.
# You are given a string sentence representing a sentence and an integer discount. For each word representing a price, apply a discount of discount% on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

# Return a string representing the modified sentence.

# Note that all prices will contain at most 10 digits.

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:

        S = sentence.split(" ")
        
        for i, s in enumerate(S):
            j = 0
            if s[j] == '$':
                j += 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                if j == len(s) and j != 1:
                    digit = int(s[1:j])
                    digit *= ((100 - discount) / 100)
                    digit = format(digit, '.2f')
                    S[i] = '$' + str(digit)
        return " ".join(S)
