
from tracemalloc import start
import unittest
import time

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # initialize queue (List) to hold root node
        queue = [self]

        while len(queue) > 0:
            # first in-first out
            current = queue.pop(0)
            # append the name of the current node to the array
            array.append(current.name)
            # append all the children of the node to the queue
            for child in current.children:
                queue.append(child)
        # queue empty, lets return the array
        return array;


    # Time Complexity  :  O(V + E) We traverse every vertex and every node (edge)
    # Space Complexity :  O(V) worst case, our queue will have V-1, and we're returning a V


class TestProgram(unittest.TestCase):
    def test_case_01(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])


def main() -> None:
    # start the timer
    startTime = time.process_time()
    
    # let's make the graph tree
    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")

    print(graph.breadthFirstSearch([]))
    endTime = time.process_time()
    print("Execution time ---", (endTime - startTime), "---")
    #print("--- %s seconds ---" % (endTime - startTime))

if __name__ == "__main__":
    main()

