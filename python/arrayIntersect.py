from matplotlib import collections
from pyparsing import nums


class Solution(object):
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = collections.Counter(nums1) & collections.Counter(nums2)
        ans = []
        for k, v in c.items():
            ans.extend([k] * v)
        return ans;

def main() -> None:
    firstArray = [4,9,5,4,4]
    secondArray = [9,4,9,8,4]
    # Initialize the class 
    mySolution = Solution();

    return 0;

if __name__ == "__main__":
    main()