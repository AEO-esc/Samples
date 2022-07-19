class Solution(object):
    def is_perfectCube(self, number) -> bool:
        """
        Returns true/false if a number is a perfect cube
        """
        number = abs(number)
        return round(number ** (1/3)) **3 == number
    # O(1) runtime since we are calculating in place
    # O(1) storage as we are not storing any values

def main() -> None:
    # initialize class
    mySolution = Solution();
    # initialize variables
    values = [3,27,81,100,1728,4539,59319,216100]
    is_cube = False

    # loop thru array and find perfect cubes
    for value in values:
        is_cube = mySolution.is_perfectCube(value)
        if is_cube:
            print(value, 'is a perfect cube!')
        else:
            print(value, 'is not a perfect cube.')

if __name__ == "__main__":
    main()
