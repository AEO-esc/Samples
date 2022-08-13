import unittest

"""
currentNode  = i
childNote    = 2i + 1
childTwo     = 2i + 2
parentNode   = (i - 1) // 2
"""

# create minimum binary heap class
class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
    def buildHeap(self, array):
        pass
    def siftDown(self):
        pass
    def siftUp(self):
        pass
    def peek(self):
        pass
    def remove(self):
        pass
    def insert(self, value):
        pass

"""Unit testing for the binary minimal heap class

Args:
    MinHeap (Class object)

Returns:
    boolean: Pass or Fail

"""
def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False;
    return True;

class TestProgram(unittest.TestCase):
    def test_case_01(self):
        minHeap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
        minHeap.insert(76)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), -5)
        self.assertEqual(minHeap.remove(), -5)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 2)
        self.assertEqual(minHeap.remove(), 2)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))
        self.assertEqual(minHeap.peek(), 6)
        minHeap.insert(87)
        self.assertTrue(isMinHeapPropertySatisfied(minHeap.heap))


def main() ->None:
    pass

if __name__ == "__main__":
    main()