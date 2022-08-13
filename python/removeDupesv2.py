class Solution(object):
    def removeDuplicates(self, nums):
        insertIndex = 0
        if (len(nums) == 0):
            return 0;
        for i in range(0, len(nums)):
            if nums[i] != nums[i - 1]:
                # this is a new number and we want to move it to index
                nums[insertIndex] = nums[i]
                # increment index
                insertIndex += 1
        print(nums[0:insertIndex])      
        return insertIndex;

def main() -> None:
    nums = [0,0,1,1,1,2,2,3,3,3,4,5,6,6,6,6,7]
    temp = Solution()
    print(temp.removeDuplicates(nums))

if __name__ == '__main__':
    main()