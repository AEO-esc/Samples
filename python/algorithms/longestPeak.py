def longestPeak(array):
    # find local peaks
    for i in range(1, len(array) - 1):
        if (array[i] > array[i - 1]) and (array[i] > array[i + 1]):
            print(array[i], "is a local peak.")

def main() -> None:
    text = 'Longest Peak'
    print(f'{text:.^20}')

    array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    print(longestPeak(array))


if __name__ == "__main__":
    main()
