from typing import List
import unittest

class Solution():
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass
    def bruteForce(self, nums: List[int], target: int)-> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
        # Time Complexity: O(n^2) since we have nested for loops
        # Space Complexity: O(1) since we are using constant space
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        # fill our hashmap with the values
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap and hashMap[complement] != i:
                return [i, hashMap[complement]];
        # Time Complexity: O(n) we traverse the array once
        # Space Complexity: O(n) since, worst case, we are storing n elements in hash
    def twoSumHash1Pass(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [i, hashMap[complement]]
            hashMap[nums[i]] = i

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        expected = [1,2]
        actual = Solution.twoSum([2,7,11,15], 18)
        self.assertEqual(expected, actual)
    def test_case_02(self):
        expected = [1,2]
        actual = Solution.twoSumHash([2,7,11,15], 18)
        self.assertEqual(expected, actual)
    def test_case_03(self):
        expected = [1,2]
        actual = Solution.twoSumHash1Pass([2,7,11,15], 18)
        self.assertEqual(expected, actual)


def main() ->None:
    #initialize class
    mySolution = Solution()
    nums =[2,7,11,15]
    target = 18

    print(mySolution.twoSum(nums, target))
    print(mySolution.bruteForce(nums, target))
    print(mySolution.twoSumHash(nums, target))
    print(mySolution.twoSumHash1Pass(nums, target))

if __name__ == "__main__":
    main()

