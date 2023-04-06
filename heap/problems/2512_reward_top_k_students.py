# You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

# Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

# You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. 
# The ID of each student is unique.

# Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        heap = []
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)

        for i, r in zip(student_id, report):
            currScore = 0
            word_list = r.split(" ")
            for w in word_list:
                if w in positive_feedback:
                    currScore -= 3
                elif w in negative_feedback:
                    currScore += 1
            heapq.heappush(heap, [currScore, i])

        ans = []
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans

