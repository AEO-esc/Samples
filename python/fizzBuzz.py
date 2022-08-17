def fizzBuzz(n):
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print ('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i += 1

def main() ->None:
    #print(fizzBuzz(1))
    #print(fizzBuzz(2))
    #print(fizzBuzz(3))
    #print(fizzBuzz(5))
    print(fizzBuzz(15))

if __name__ == '__main__':
    main()