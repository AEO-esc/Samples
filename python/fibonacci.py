import unittest

class Solution():
    def getNthFib(n, dict ={1:0, 2:1}):
        if n in dict:
            return dict[n]
        else:
            dict[n] = Solution.getNthFib(n - 1, dict) + Solution.getNthFib(n - 2, dict)
            return dict[n]
        # Time Complexity: O(n)
        # Space Complexity: O(n)


    def getNthFibRecursive(n):
        if n == 1:
            return 0;
        elif n == 2:
            return 1;
        else:
            return Solution.getNthFibRecursive(n - 1) + Solution.getNthFibRecursive(n - 2)
        # Time Complexity: O(2^n) since every time we split, we add 'n' computations
        # Space Complexity: O(n) since this is a recursive function and are using 'n' call stacks
    
    def getNthFibIterative(n):
        lastTwo = [0, 1]
        counter = 3
        while counter <= n:
            nextFib = lastTwo[0] + lastTwo[1]
            lastTwo[0] = lastTwo[1]
            lastTwo[1] = nextFib
            counter += 1
        if n > 1:
            return lastTwo[1];
        else:
            return lastTwo[0]
        
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        

def main()-> None:
    print(Solution.getNthFibIterative(6))

if __name__ == '__main__':
    main()

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        expected = 5
        actual = Solution.getNthFib(6)
        self.assertEqual(actual, expected)
    def test_case_02(self):
        expected = 5
        actual = Solution.getNthFibRecursive(6)
        self.assertEqual(expected, actual)