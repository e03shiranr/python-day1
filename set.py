print("--- Set Operation ---")
set_a = {10, 20, 30, 40, 50}
set_b = {40, 50, 60, 70, 80}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

union_set = set_a.union(set_b)
print(f"Union of set_a and set_b is: {union_set}")

intersection_set = set_a.intersection(set_b)
print(f"Intersection of set_a and set_b is: {intersection_set}")
