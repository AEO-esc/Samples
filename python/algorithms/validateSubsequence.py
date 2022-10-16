from msilib import sequence


def isValidSubsequnceWhileLoop(array, sequence):
    arrayIndex = 0
    sequenceIndex = 0

    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        # increase sequence index if we found a match
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        # regardless if we found a match, advance one space
        arrayIndex += 1
    # we've iterated thru the entire sequence so we found a valid sub-sequence
    return sequenceIndex == len(sequence);

    # Time Complexity: O(n) since, worst-case, we need to iterate through all n elements of array
    # Space Complexity: O(1) since we are not storing anything; constant space

def isValidSubsequenceForLoop(array, sequence):
    sequenceIndex = 0
    for value in array:
        if sequenceIndex == len(sequence):
            return True
        if sequence[sequenceIndex] == value:
            sequenceIndex += 1
    return sequenceIndex == len(sequence)

    # Time Complexity: O(n) since, worst-case, we need to iterate through all n elements of array
    # Space Complexity: O(1) since we are not storing anything; constant space

def main() -> None:
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequnceWhileLoop(array, sequence))
    

if __name__ == "__main__":
    main()