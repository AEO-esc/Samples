from typing import List
from unicodedata import digit


class Solution(object):
    def plusOne(self, digits):
        digitLength = len(digits)
        # move along the input array starting from the end
        for i in range(digitLength):
            index = digitLength - 1 - i
            # set all the nines at the end of the array to zeros
            if digits[index] == 9:
                digits[index] = 0
            # here we have the rightmost not-nine
            else:
                # increase this rightmost not-nine by 1
                digits[index] += 1
                return digits
        # all digits were nine
        return [1] + digits
    # Time Complexity: O(n) since we are passing through the array just once
    # Space Complexity: O(n) since we are storing N+1 elements

    def plusOneArray(self, digits):
        for i in range( len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits;
        digits[i] = 0;

        
def main() -> None:
    # initialize class
    mySolution = Solution()
    solutionArray = [9,9,9]
    
    print(mySolution.plusOne(solutionArray))
    #print(mySolution.plusOneArray(solutionArray))
    return 0;

if __name__ == "__main__":
    main();