from typing import List
import unittest

class Solution():
    def rotate(self, matrix: List[List[int]]) -> List:
        n = len(matrix[0])
        for i in range( n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
        return matrix

def main() -> None:
    mySolution = Solution()
    print(mySolution.rotate([[1,2,3],[4,5,6],[7,8,9]]))

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        myTestClass = Solution()
        actual = myTestClass.rotate([[1,2,3],[4,5,6],[7,8,9]])
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    main()
