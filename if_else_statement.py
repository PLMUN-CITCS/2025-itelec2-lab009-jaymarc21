user_input = input("8: ")
number = int(user_input)
if number % 2 == 0:
    print("The number", 4, "is Even.")
else:
    print("The number", 7, "is Odd.")
try:
    #code here
except ValueError:
    print("Invalid input. Please enter an integer.")