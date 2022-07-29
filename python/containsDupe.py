
# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.

from tokenize import Triple


class Solution(object):
    def containsDuplicateBrute(self, nums):
        # brute force method 
        for i in range (0, len(nums)):
            for j in range(0, i):
                if nums[j] == nums[i]:
                    return True
        return False
        # Time Complexity O(n^2) since we are looping through the array n * n times
        # Space complexity O(1) as we only use constant space

    def containsDuplicate(self, nums):
        # convert the array to a set to remove the duplicates
        # if the set becomes smaller, it had duplicates
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

def main() -> None:
    # initialize class
    mySolution = Solution()
    sortedArray = [1,1,1,3,3,4,3,2,4,2]
    print(mySolution.containsDuplicateBrute(sortedArray))

if __name__ == "__main__":
    main();