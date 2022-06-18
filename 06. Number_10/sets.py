# list - []
# tuple - ()
# set - {}
# dict - {key: value}

set1 = {2, 3, 4, 5, 6, 7, 8, 9, 9, "Try", "Delete"}
set2 = {True, False, "Try", "Delete"}

set_union = set1.union(set2)

forzen_set_1 = frozenset(set1)

# forzen_set_1.add("Print")
set1.add("Print")

print("Set 1: ", set1)
print("Set 2: ", set2)

print("Set Union: ", set_union)

set_intersection = set1.intersection(set2)

print("Set Intersection: ", set_intersection)