import unittest

# Create dictonary data structure for lookup
lookupTable = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:
    def romanToInt(s):
        total = 0;
        i = 0;
        while i < len(s):
            # If the roman numeral needs to be subtracted 
            if (i + 1 < len(s)) and (lookupTable[s[i]] < lookupTable[s[i + 1]]):
                total += lookupTable[s[i + 1]] - lookupTable[s[i]]
                i += 2; # jump ahead by 2
            # No subtraction so continue as normal
            else:
                total += lookupTable[s[i]]
                i += 1; # jump ahead
        return total;

        # Time Complexity: O(1) since we are utilizing a lookup table
        # Space Complexity: O(1) since we are using a constant number of sinle-variable lookiups

"""Unit testing for the Roman Integer to Integer class & function
Args:
    A valid array of letter that can be used as Roman integers
Returns:
    boolean: Pass or Fail if it equals the integer the Roman numeral is valued at
"""

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        self.assertEqual(Solution.romanToInt('MCMXCIV'), 1994)
    def test_case_02(self):
        self.assertEqual(Solution.romanToInt('LVIII'), 58)
    def test_case_03(self):
        self.assertEqual(Solution.romanToInt('MMMCMXCIX'), 3999)

def main() ->None:
    roman = input("Enter a Roman numeral: ")
    print("Your Roman numeral is: ", Solution.romanToInt(roman))

if __name__ =="__main__":
    main()