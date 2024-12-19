# create a variable to store the user input
weather = input("What is the like today? (sunny/rainny/cold): ")
if weather == "sunny":
    print("Wear a T-shirt and sunglasses")
elif weather == "rainny":
    print("Dont forget your umbrella and a raincoat")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Invalid input. Please enter sunny, rainny, or cold.")