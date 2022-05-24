class Solution:
    def is_perfectCube(number) -> bool:
        """
        Returns true/false if a number is a perfect cube
        """
        number = abs(number)
        return round(number ** (1/3)) **3 == number

    values = [3,27,81,100,1728,4539,59319,216100]
    for value in values:
        is_cube = is_perfectCube(value)
        if is_cube:
            print(value, 'is a perfect cube!')
