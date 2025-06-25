print("--- Set Operation ---")
set_a = {10, 20, 30, 40, 50, 60, 70}
set_b = {40, 50, 60, 70, 80, 90}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

union_set = set_a.union(set_b)
print(f"Union of set_a and set_b is: {union_set}")

intersection_set = set_a.intersection(set_b)
print(f"Intersection of set_a and set_b is: {intersection_set}")

difference_set = set_a.difference(set_b)
print(f"Differece (set a - set b): {difference_set}")
print("\n -- List De-duplication using Sets ---")

my_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(f"Original list with duplicates: {my_list}")

unique_elements_set = set(my_list)
print(f"Set created from list is: {unique_elements_set}")

unique_set = list(unique_elements_set)
print(f"list conveted to Set: {unique_set}")