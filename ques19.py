# Remove duplicate elements
my_tuple = (10, 20, 10, 30, 20, 40, 30)

result = tuple(dict.fromkeys(my_tuple))

print("Tuple without duplicates:", result) 