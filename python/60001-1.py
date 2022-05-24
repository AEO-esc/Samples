# Create a variable 3 and assign a value 3 to it
x = 3 
# Bind X to value 9
x = 9
print(x)
# Print the type of letter y
print(type('y'))

# Print an input from user
y = input('Enter an input: ')
print('Your input is ' + y)

# find if a number is even or odd
z = int(input('Enter an integer: '))

if z % 2 == 0:
    print(z, ' is Even')
else:
    print(str(z) + ' is Odd')

# Find the cude root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0

while ans*ans*ans < abs(x):
    ans = ans + 1
    if ans*ans*ans != abs(x):
        print(x, ' is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ', ans) 
