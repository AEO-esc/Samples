class Solution(object):
        # Time: O(n)
        # Space: O(1)
    def removeDuplicates(self, nums):


        n = len(nums)
        if n == 0:
            return 0;

        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i -1]:
                nums[insertIndex] = nums[i]
                insertIndex += 1
        print(nums[0:insertIndex])
        return insertIndex;


def main() -> None:
    nums = [0,0,1,1,1,2,2,3,3,4]
    temp = Solution()
    print("K is equal to:", temp.removeDuplicates(nums))

if __name__ == '__main__':
    main()