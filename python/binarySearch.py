import unittest
from numpy import array
import unittest


class Solution(object):
    def binarySearch(self, array, target):
        #return Solution.binaryRecursiveSearchHelper(array, target, 0, len(array) - 1)
        return Solution.binaryIterativeSearchHelper(array, target, 0, len(array) - 1)
    
    # Time Complexity:  O(log(n)). We are eliminating half the inputs every search
    # Space Complecity: O(log(n)). We are using recursive calls

    def binaryRecursiveSearchHelper(array, target, left, right):
        # we didn't find the number we're searching for
        if left > right:
            return 0;
        middle = (left + right) // 2
        potentialMatch = array[middle]

        if target == potentialMatch:
            return middle;
        # eliminate the right half of the array
        elif target < potentialMatch:
            return Solution.binaryRecursiveSearchHelper(array, target, left, middle - 1)
        else: # eliinate the left half of the array
            return Solution.binaryRecursiveSearchHelper(array, target, middle + 1, right)
    
    def binaryIterativeSearchHelper(array, target, left, right):
        # divide and conquer
        while left <= right:
            middle = (left + right) // 2
            potentialMatch = array[middle]
            if target == potentialMatch:
                return middle;
            # remove the right half of the array
            elif target < potentialMatch:
                right = middle - 1
            # remove the left half of the array
            else:
                left = middle + 1
        # number not found
        return -1;
        # Time Complexity:  O(log(n)). We are eliminating half the inputs every search
        # Space Complecity: O(1). We are using constant space

    def binarySearch2(self, array, target):
        # divide and conquer
        left = 0
        right = len(array) -1
        

        while left <= right:
            middle = (left + right) // 2
            potentialMatch = array[middle]
            if target == potentialMatch:
                return middle;
            elif target < potentialMatch:
                # elininate the right side of array
                right = middle - 1
            else:
                # elininate the left side of array
                left = middle + 1
        # no match found
        return -1;

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tester = Solution();
        self.assertEqual(tester.binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)


def main() -> None:
    #initialize class
    mySolution = Solution();
    solutionArray = [0,1,21,33,45,45,61,71,72,73]
    searchValue = 33

    print(mySolution.binarySearch(solutionArray, searchValue))
    #print(mySolution.binarySearch2(array, searchValue))

if __name__ == "__main__":
    main()