# Find the index of an element
my_tuple = (10, 20, 30, 40, 50)

number = int(input("Enter a number: "))

if number in my_tuple:
    print("Index:", my_tuple.index(number))
else:
    print("Element not found")