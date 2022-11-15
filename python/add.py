from time import sleep, time
import unittest

def add(num1, num2):
    """
    adds two positive integers
    not very fast tho
    """
    start = time()
    sleep(num1)
    sleep(num2)

    return int(time() - start)

class TestProgram(unittest.TestCase):
    def TestCase1(self):
        expected = 10
        actual = add(5,5)
        self.assertEqual(expected, actual)

def main() -> None:
    print(add(500, 500))

if __name__ == "__main__":
    main()