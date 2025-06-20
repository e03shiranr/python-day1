num_int = 10
num_float = float(num_int)
num_str = str(num_int)
formatted_float = round(num_float,2)

print(f"Original Integer : {num_int}, Type: {type(num_int)}")
print(f"Convert to Float : {num_float}, Type: {type(num_float)}")
print(f"Convert to String : {num_str}, Type: {type(num_str)}")
print(f"Convert to float 2 digit : {formatted_float}, Type: {type(formatted_float)}")