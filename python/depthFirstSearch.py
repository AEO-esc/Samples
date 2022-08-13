import unittest

class Node:
    def __init__(self, name):
        self.children =[]
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

        # Time Complexity: O(V + E), worst case, we are looking at all vertices and edges
        # Space Complecity: O(V). Worst case, we store all vertices

# Unit testing
class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A");
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.depthFirstSearch([]), ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])


def main() -> None:
    myTest = TestProgram()
    print( myTest.test_case_1())
    #print(Node.depthFirstSearch("I"))

if __name__ == "__main__":
    main()