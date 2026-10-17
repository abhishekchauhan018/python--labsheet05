# Find repeated items
my_tuple = (10, 20, 10, 30, 20, 40, 10)

repeated = tuple(
    item for i, item in enumerate(my_tuple)
    if item in my_tuple[:i] and item not in my_tuple[:my_tuple.index(item)]
)

# Use count() to identify each repeated item only once
repeated = tuple(
    item for i, item in enumerate(my_tuple)
    if my_tuple.count(item) > 1 and item not in my_tuple[:i]
)

print("Repeated items:", repeated)