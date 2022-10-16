import unittest

class Solution():
    def isPalindrome(self, s) -> bool:
        left, right, = 0, len(s)-1

        while left < right:
            # filter out non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            # convert remaining characters to lower-case 
            # characters should be equal if palindrome
            if s[left].lower() != s[right].lower():
                return False

            # start at the begining
            left += 1
            # start at the end
            right -= 1

        return True;
        # Time Complexity: O(n). We traverse over each character 
        # at least once until we meet in the middle
        # Space Complexity: O(1). No extra space, static pointers

def main() -> None:
    # initialize class
    mySolution = Solution()
    s = "A man, a plan, a canal: Panama"

    print(mySolution.isPalindrome(s))

if __name__ == "__main__":
    main()

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = "A man, a plan, a canal: Panama"
        expected = True
        actual = Solution.isPalindrome(input)
        self.assertEqual(actual, expected)