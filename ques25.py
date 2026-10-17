# Find elements present in tuple1 but not tuple2
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

difference = tuple(x for x in tuple1 if x not in tuple2)

print("Difference:", difference)