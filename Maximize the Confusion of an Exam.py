class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        maximum_number = 0
        count_False = 0
        count_True = 0
        for right in range(len(answerKey)):
            if answerKey[right] == 'F':
                count_False += 1
            else:
                count_True += 1

            while count_False > k and count_True > k:
                count_False -= 1 if answerKey[left] == 'F' else 0
                count_True -= 1 if answerKey[left] == 'T' else 0
                left += 1
            w = right - left + 1
            maximum_number = max(w, maximum_number)
        return maximum_number
