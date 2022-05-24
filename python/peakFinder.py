# Time complexity of O(n) time
# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/
# https://medium.com/theengineeringgecko/finding-a-peak-f2d833525d31
import unittest

class SimpleTest(unittest.TestCase()):
    def test(self):
        self.assertTrue(True)

class Solution(object):
    def findLinearPeakElement(list):
        # Linear search; scan the list for a peak
        # Time complexity: O(n). We traverse the nums array of size n once only
        # Space complexity: O(1). Constant extra space is used
        # returns the index and value if a peak is found
        for i in range(1, len(list) - 1):
            if (list[i] > list[i - 1] and list[i] > list[i + 1]):
                return i, list[i];
    def findPeakBinarySearch (list, low, high, size):
        # Binary recursive search
        # Time complexity:  O(log(n))
        # Space Complexity: O(1)

        # get the middle of the array
        middle = low + (high - low) / 2
        middle = int(middle)

        # check the middle index against it's neighbors
        if(
            (middle == 0 or list[middle - 1] <= list[middle])  and
            (middle == size - 1 or list[middle + 1] <= list[middle])
        ):
            return middle;
        # Left side is bigger. Recursive search the left side of the array for peak
        elif (middle > 0 and list[middle - 1] > list[middle]):
            return Solution.findPeakBinarySearch(list, low, middle - 1, size);
        #Right side is bigger. Recursive search the right side of the array for peak
        else:
            return Solution.findPeakBinarySearch(list, (middle + 1), high, size);
            
array = [6,6,4,3,9,1,4,5]
low = 0
high = len(array)     
size = len(array)
print('Index and value of array is',Solution.findLinearPeakElement(array))
print('Binary search peak at index:', Solution.findPeakBinarySearch(array, low, high, size))
#print("Index of peak point is at ", Solution.findPeakElemnt(nums))
#print("Index of peak element is at index ", Solution.findBetterPeakElement(nums))