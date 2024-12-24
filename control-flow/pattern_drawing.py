# promt the user to enter the a positive number
size = int(input("Enter the size of the pattern: "))
row = 0

# loop through each row using a while loop
while row < size:
    
    # use a for loop to  print the astericks
    for i in range(size):
        print("*", end="")
    print()
    row += 1