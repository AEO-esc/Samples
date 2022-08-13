from cgi import print_environ_usage


class Solution():
    def rotate(self, nums, k):
        n = len(nums)
        # Lets use a temp array
        a = [0] * n

        for i in range(n):
            a[(i + k) % n] = nums[i]
        # copy original array to new one
        nums[:] = a
        return a;
    # Time Complexity: O(n) since we traverse the array once
    # Space Complexity: O(n) since we made another array of same size

    def bruteForce(self, nums, k):
        k = k % len(nums)

        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
                


def main() -> None:
    # Initialize class
    temp = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 6
    print(temp.rotate(nums, k))

if __name__ == '__main__':
    main();