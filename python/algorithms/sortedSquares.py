import unittest

def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerIndex = 0
    largerIndex = len(array) - 1
    # start from the end of the array and go backwards
    for index in reversed(range(len(array))):
        smallerValue = array[smallerIndex]
        largerValue = array[largerIndex]

        if abs(smallerValue) > abs(largerValue):
            # left side of array is larger, add squared root on place and advance 1 to right
            sortedSquares[index] = smallerValue * smallerValue
            smallerIndex += 1
        else:
            # right side of array is larger, add squared root in place and advance 1 to left
            sortedSquares[index] = largerValue * largerValue
            largerIndex -= 1
    return sortedSquares

    # Time Complexity: O(n) as we iterate thru n elements
    # Space Complexity: O(n) since we are creating a new array of n elements

def sortedSquaredArraywithSort(array):
    # initialize array with zeros
    sortedSquares = [0 for _ in array]

    for index in range(len(array)):
        value = array[index]
        sortedSquares[index] = value * value
    # binary sort
    sortedSquares.sort()
    return sortedSquares

    # Time Complexity: O(nLog(n)) since we are using a sorting array (binary sort)
    # Space Complexity: O(n) since we are storing a new array of n elements

def main() ->None:
    array1 = [1, 2, 3, 5, 6, 8, 9]
    array2 = [-4, 1, 2]
    array3 = [-7, -5, -4, 3, 6, 8, 9]
    print(sortedSquaredArray(array1))
    print(sortedSquaredArray(array2))
    print(sortedSquaredArray(array3))

if __name__ == "__main__":
    main()

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 91]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)
    def test_case_02(self):
        input = [-4, 1, 2]
        expected = [1, 4, 16]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)
    def test_case_02(self):
        input = [-7, -5, -4, 3, 6, 8, 9]
        expected = [9, 16, 25, 36, 49, 64, 91]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)