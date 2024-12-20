
# create a viriable to store the user input
num1 = int(input("Enter a number to see its multiplication table: "))

# print the multiplication table for the given number
# print(f'multiplication table for {num1} is: ')

# loop through the range from 1 to 10 (inclusive) and calculate the product for each number
for i in range(1,11):
    # culculate the product of the number enterd and the range 
    product = num1 * i
    # print the result.
    print(f'{num1} * {i} = {product}')
    print()