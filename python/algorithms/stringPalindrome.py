def isPalindromeString(string):
    reversedString = ""

    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

    # Time Complexity: O(n^2) time as we are using string concatenation
    # Space Complexity: O(n) space as we are storing a new string of n size

def isPalindromeArray(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)

    # Time Complexity: O(n) since iterate thru n elements
    # Space Complexity: O(n) space since we are storing a new array of n elements

def isPalindromeOptimal(string):
    pass


def main() -> None:
    pass

if __name__ == "__main__":
    main()