
from array import array
from functools import total_ordering


def arraySum(numbers):
    totalSum = 0

    for i in range(0, len(numbers)-1):
        totalSum += numbers[i]
    return totalSum;

def main() ->None:
    myNumbers = [1,2,3,4,5]
    print(arraySum(myNumbers))



if __name__ == '__main__':
    main()