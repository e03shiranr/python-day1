import csv
csv_file_name = "employee.csv"
target_department = "IT"
print(f"Attempting to read employees from {csv_file_name} and")

filterred_emplyees =[]

try:
    with open(csv_file_name, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row.get('Department') == target_department:
                filterred_emplyees.append(row)
    print(f"Filtered employee List: {filterred_emplyees}")
    
#    print(f"\n--- Employees in the {target_department} Department ---")
#   if filterred_emplyees:
#       print

except FileNotFoundError:
    print(f"Eroor: The csv file {csv_file_name} was not found")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
