from collections import deque
import unittest

class Solution(object):
    def reverseWords(self, s:str) -> str:
        # split the sentence into words
        words = s.split(' ')
        # reverse the string and join with whitespace
        reversedSentence = ' '.join(reversed(words))
        # returned the reversed words as a string
        return reversedSentence;

    def reverseDequeue(self, s:str) -> str:
        left = 0
        right = len(s) - 1
        # lets remove whitespace
        while left <= right and s[left] == ' ':
            left -= 1
        # lets remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        d = deque()
        word = []
        # push word by word in front of dequeue
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)
    
    # Time Complexity: O(N), since we are scanning through N elements
    # Space Complexity: O(N) as we are storing the split words

def main() -> None:
    sentence = "the sky is blue"
    mySolution = Solution()
    print(mySolution.reverseWords(sentence));

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        # initialize solution
        myTestSolution = Solution()
        actual = myTestSolution.reverseWords("the sky is blue")
        expected = "blue is sky the"
        self.assertEqual(actual, expected)
    def test_case_02(self):
        myTestSolution = Solution()
        actual = myTestSolution.reverseWords("code practice quiz")
        expected = "quiz practice code"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    main();