# Check whether an element exists
my_tuple = (10, 20, 30, 40, 50)

number = int(input("Enter a number: "))

if number in my_tuple:
    print("Element exists in tuple")
else:
    print("Element does not exist in tuple")