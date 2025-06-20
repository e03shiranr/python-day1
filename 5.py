str_num = 25.951
float_num = float(str_num)
int_num = int(str_num)
formatted_float = round(float_num,2)

print(f"Original String : {str_num}, Type: {type(str_num)}")
print(f"Convert to Float : {float_num}, Type: {type(float_num)}")
print(f"Convert to Integer : {int_num}, Type: {type(int_num)}")
print(f"Convert to float 2 digit : {formatted_float}, Type: {type(formatted_float)}")