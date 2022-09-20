import unittest

class Calculator():
    def calcHelper(operation, num1, num2):
        if (num1.isnumeric() and num2.isnumeric()):
            if operation == "ADD":
                Calculator.calcAdd(int(num1), int(num2));
            elif operation == "SUB":
                Calculator.calcSubtract(int(num1), int(num2));
            elif operation == "MULT":
                Calculator.calcMultiply(int(num1), int(num2));
            elif operation == "DIV":
                Calculator.calcDivide(int(num1), int(num2))
            elif operation == "MOD":
                Calculator.calcModulus(int(num1), int(num2))
            elif operation == "ESC":
                return;
            else:
                print("Bad selecttion.")
        else:
            print("Bad numbers entered.")

    def calcAdd(a, b):
        answer = a + b
        print(str(a),"+",str(b),"=", str(answer), "\n")
        return answer;
    def calcSubtract(a, b):
        answer = a - b
        print(str(a),"-",str(b),"=", str(answer), "\n")
        return answer;
    def calcMultiply(a, b):
        answer = a * b
        print(str(a),"*",str(b),"=", str(answer), "\n")
        return answer;
    def calcDivide(a, b):
        answer = a / b;
        print(str(a),"/",str(b),"=", str(answer), "\n")
        return answer;
    def calcModulus(a, b):
        answer = a % b;
        print(str(a),"%",str(b),"=", str(answer), "\n")
        return answer;

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        expected = 11
        actual = Calculator.calcAdd(5,6)
        print(actual)
        self.assertEqual(actual, expected)
    def test_case_2(self):
        expected = 3
        actual = Calculator.calcSubtract(10,7)
        self.assertEqual(actual, expected)
    def test_case_3(self):
        expected = 12
        actual = Calculator.calcMultiply(3,4)
        self.assertEqual(actual, expected)
    def test_case_4(self):
        expected = 20
        actual = Calculator.calcDivide(100, 5)
        self.assertEqual(actual, expected)
    def test_case_5(self):
        expected = 1
        actual = Calculator.calcModulus(10,3)
        self.assertEqual(actual, expected)

def main() -> None:
    math = input("Would you like to ADD, SUB, MULT, DIV, or MOD?")
    firstNumber = input("Enter the first number:")
    secondNumber = input("Enter the second number:")
    Calculator.calcHelper(math, firstNumber, secondNumber)
    TestProgram.test_case_1();

if __name__ == "__main__":
    main();

