from this import s
from turtle import left, right


class Solution(object):
    def reverseString(self, s):
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            # move leftPointer one step right 
            # move rightPointer one step left
            s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
            leftPointer, rightPointer = leftPointer + 1, rightPointer - 1
        return s;
    
        # Time Complexity: O(n) to swap N elements 
        # Space Complexity: O(1) as we are doing swaps in constant space

def main() -> None:
    arrayToReverse = ['h','e', 'l','l','o']
    # initialize class
    mySolution = Solution();

    # Call the class and print to screen 
    print(mySolution.reverseString(arrayToReverse))

if __name__ == "__main__":
    main();