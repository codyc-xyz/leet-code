# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. 
# He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. 
# In addition, you are given an integer k, the maximum number of times you may perform the following operation:
# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tWindowStart = fWindowStart = 0
        tK = fK = k
        tMax = fMax = 0
        for tWindowEnd in range(len(answerKey)):
            if answerKey[tWindowEnd] == 'F':
                tK -= 1
            if tK < 0:
                if answerKey[tWindowStart] == 'F':
                    tK += 1
                tWindowStart += 1
            tMax = max(tMax, tWindowEnd - tWindowStart + 1)
        for fWindowEnd in range(len(answerKey)):
            if answerKey[fWindowEnd] == 'T':
                fK -= 1
            if fK < 0:
                if answerKey[fWindowStart] == 'T':
                    fK += 1
                fWindowStart += 1
            fMax = max(fMax, fWindowEnd - fWindowStart + 1)
        return max(tMax, fMax)


