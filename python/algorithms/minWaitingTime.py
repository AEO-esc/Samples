import unittest

class TestProgram(unittest.TestCase):
    def testCase1(self):
        queries = [3, 2, 1, 2 ,6]
        expected = 17
        actual = minimumWaitingTime(queries)
        self.assertEqual(actual, expected)

def minimumWaitingTime(queries):
    # sort input array
    queries.sort()
    totalWait = 0
    
    # greedy algorithm - let's execute the smallest queries first
    for index, duration in enumerate(queries):
        queriesLeft = len(queries) - (index + 1)
        totalWait += duration * queriesLeft
    return totalWait  
    # Time  Complexity: O(n log(n)) since we are using a binary sort
    # Space Complexity: O(1) constant since we are not storing any data

def main() ->None:
    queries = [3, 2, 1, 2 ,6]
    print(minimumWaitingTime(queries))

if __name__ == "__main__":
    main()