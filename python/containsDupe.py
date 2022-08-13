class Solution():
    def containsDuplicate(self, nums):
        # Brute force method
        for i in range(0, len(nums)):
            for j in range(0, i):
                if(nums[j] == nums[i]):
                    return True
        return False
    # Time Complexity O(n ^2): Worst case is n(n-1)/2
    # Space Complexity is O(1) as we only used constant extra space

    def containsDuplicateSorted(self, nums):
        # lets use Python's internal sort function
        sort = sorted(nums)

        # Since the array is sorted, we can check neighbor for dupe
        for i in range(0, len(sort) - 1):
            if sort[i] == sort[i + 1]:
                return True;

        return False;
        # Time Complexity O(n log n) since the heapsort takes the majority of the time.
        # Space Complexity O(1) since heapsort is used

def main() -> None:
    nums = [1,1,1,3,3,4,3,2,4,2]
    nums2 = [1,2,3,4,5,6,7,8,9,10]
    #initialize class
    temp = Solution()
    print(temp.containsDuplicate(nums2))
    print(temp.containsDuplicateSorted(nums))
    print(temp.containsDuplicateSorted(nums2))

if __name__ == '__main__':
    main()