favourite_number_str = input("Please enter your favorite String:")
try:
    converted_number = int(favourite_number_str)
    print(f"\nSuccesfully Converted input to Integer: {converted_number}")
    final_result_int = converted_number + 10
    print(f"\nResult After adding 10(integer): {final_result_int}, Type: type{final_result_int}")

except ValueError:
    try:
        converted_number = float(favourite_number_str)
        print(f"\nSuccesfully Converted input to Float: {converted_number}")
        final_result_int = converted_number + 10
        print(f"\nResult After adding 10(float): {final_result_int}, Type: type{final_result_int}")
    except ValueError:
        print(f"\nInvalid input: '{favourite_number_str}'cannot be converted")
