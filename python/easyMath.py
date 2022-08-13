class Solution(object):
    def Addition(self, x, y):
        return x + y
    def Subtraction(self, x, y):
        return x - y
    def Multiplication(self, x, y):
        return x * y
    def Division(self, x, y):
        return x / y
    def Modulus(self, x, y):
        return x % y

def main() -> None:
    # Initialize class
    temp = Solution() 

    a = int(input("Enter a numer: "))
    b = int(input("Enter another number: "))

    print("Addition is: ", temp.Addition(a, b));
    print("Subtraction is ", temp.Subtraction(a, b));
    print("Multiplcation is ", temp.Multiplication(a, b));
    print("Divison is ", temp.Division(a, b));
    print("Modulus is ", temp.Modulus(a, b));


if __name__ == '__main__':
    main()