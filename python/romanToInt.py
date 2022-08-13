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
        


roman = input("Enter a Roman numeral: ")
print("Your Roman numeral is: ", Solution.romanToInt(roman))