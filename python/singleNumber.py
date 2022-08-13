from collections import defaultdict
from typing import List

class Solution(object):
    def singleNumberBit(self, nums):
        a = 0
        for i in nums:
            a ^= i
            return a;
        # Time complexity: O(n) since we iterate through n nums
        # Space complexity: O(1) since it's a static number
    
    def singleNumberMath(self, nums):
        # 2*(a+b+c) - (a+a+b+b+c) = c
        return 2 * sum(set(nums)) - sum(nums);

    def hashTable(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        # Add the nums array into our hash table
        for i in nums:
            hash_table[i] += 1
        # return the element that appears only once
        for i in hash_table:
            if hash_table[i] == 1:
                return i;
        # Time complexity: O(n+n) = O(n)
        # Space complexity: O(n+n) = O(n)

def main() -> None:
    nums = [4,1,2,1,2]
    # initialize class
    temp = Solution()
    print(temp.singleNumberMath(nums))
    print(temp.hashTable(nums))
    print(temp.singleNumberBit(nums))

if __name__ == "__main__":
    main()