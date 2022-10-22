from cmath import cos, sin
import math
import unicodedata

class cube3d(object):
    def __init__(self) -> None:
        cubeWidth = 10
        width = 160
        height = 44
        zBuffer = [width * height]
        buffer = [width * height]
        backgroundASCIICode = ' '

    def calculateX(i: int , j: int, k: int):
        A, B, C = 0
        return  j * sin(A) * sin(B) * cos(C) - k * cos(A) * sin(B) * cos(C) + \
                j * cos(A) * sin(C) + k * sin(A) * sin(C) + i * cos(B) * cos(C)
    def calculateY(i: int, j: int, k: int):
        A, B, C = 0
        return j * cos(A) * cos(C) + \
            k * sin(A) * cos(C) - \
            j * sin(A) * sin(B) * sin(C) + \
            k * cos(A) * sin(B) * sin(C) - \
            i * cos(B) * sin(C)
    def calculateZ(i: int, j: int, k: int):
        A, B, C = 0
        return k * cos(A) * cos(B) - \
            j * sin(A) * cos(B) + \
            i * sin(B)

def main() -> None:
    pass

if __name__ == "__main__":
    main()