# Check whether all elements are the same
my_tuple = (5, 5, 5, 5, 5)

if len(my_tuple) > 0 and all(
    item == my_tuple[0] for item in my_tuple
):
    print("All elements are the same")
else:
    print("Elements are not all the same")