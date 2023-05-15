# There is an ATM machine that stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

# When withdrawing, the machine prioritizes using banknotes of larger values.

# For example, if you want to withdraw $300 and there are 2 $50 banknotes, 1 $100 banknote, and 1 $200 banknote, then the machine will use the $100 and $200 banknotes.
# However, if you try to withdraw $600 and there are 3 $200 banknotes and 1 $500 banknote, then the withdraw request will be rejected because the machine will first try to use the $500 banknote and then be unable to use banknotes to complete the remaining $100. Note that the machine is not allowed to use the $200 banknotes instead of the $500 banknote.
# Implement the ATM class:

# ATM() Initializes the ATM object.
# void deposit(int[] banknotesCount) Deposits new banknotes in the order $20, $50, $100, $200, and $500.
# int[] withdraw(int amount) Returns an array of length 5 of the number of banknotes that will be handed to the user in the order $20, $50, $100, $200, and $500, and update the number of banknotes in the ATM after withdrawing. Returns [-1] if it is not possible (do not withdraw any banknotes in this case).

class ATM:

    def __init__(self):
        self.amounts = [[0, 0, 20], [0, 0, 50], [0, 0, 100], [0, 0, 200], [0, 0, 500]]
        
    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
           self.amounts[i][0] += banknotesCount[i] * self.amounts[i][2]
           self.amounts[i][1] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawn = [0 for _ in range(5)]
        remaining = amount
        for i in range(len(self.amounts) - 1, -1, -1):
            banknote_count = min(self.amounts[i][1], remaining // self.amounts[i][2])
            withdrawn[i] = banknote_count
            remaining -= banknote_count * self.amounts[i][2]
            if remaining == 0:
                for j in range(len(withdrawn)):
                    self.amounts[j][1] -= withdrawn[j]
                    self.amounts[j][0] -= withdrawn[j] * self.amounts[j][2]
                return withdrawn
        return [-1]

