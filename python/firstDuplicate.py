import unittest

class Solution():
    def firstDuplicateValueBruteForce(array):
        # if the minimum index is still length of array, there is no duplicate
        minimumIndex = len(array)
        for i in range(len(array)):
            value = array[i]
            for j in range(i + 1, len(array)):
                valueToCompare = array[j]
                if value == valueToCompare:
                    # found a duplicate
                    minimumIndex = min(minimumIndex, j)
        if minimumIndex == len(array):
            # no duplicates found
            return -1;
        return array[minimumIndex]
    
        # Time complexity: O(n^2) time since we are using two nested n loops
        # Space complexity: O(1) as we are using constant space
    
    def firstDuplicateValueSet(array):
        # lets use a set data structure for quick lookups
        seen = set()
        for value in array:
            if value in seen:
                # duplicate found
                return value;
            seen.add(value)

        # no duplicate found
        return -1;

        # Time Complexity: O(n) since at worst case we run thru all n elements
        # Space Complexity: O(n) space since we could store up to 'n' elements in our set
    
    def firstDuplicateValueBest(array):
        for value in array:
            absValue = abs(value)
            if array[absValue -1] < 0:
                return absValue
            array[absValue - 1] *= -1

        # no duplicate found
        return -1

        # Time Complexity: O(n)
        # Space Complexity: O(1)

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        input = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        actual = Solution.firstDuplicateValueSet(input)
        self.assertEqual(actual, expected)

def main()->None:
    array = [2, 1, 5, 2, 3, 3, 4]
    #print(Solution.firstDuplicateValueBruteForce(array))
    print(Solution.firstDuplicateValueSet(array))
    #print(Solution.firstDuplicateValueBest(array))

if __name__ == '__main__':
    main()