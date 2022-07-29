""""
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a^=i
        return a;

    # Time Complexity: O(n) since we iterate thru nums once
    # Space Complexity: O(1) 

def main() -> None:
    mySolution = Solution()
    nums = [2,2,1,1,3,3,4,4,6]
    print(mySolution.singleNumber(nums))

if __name__ == "__main__":
    main()