try:
    numerator_input = input("Enter the numerator: ")
    numerator = float(numerator_input)
    denominator_input = input("Enter the denominator: ")
    denominator = float(denominator_input)

    result = numerator / denominator

    print (f"You entered: Numerator = {numerator}, denominator = {denominator}")
    print(f"result of the devision is : {result}")

except ValueError:
    print("Entered value is invalid. Please neter a correct value")

except ZeroDivisionError:
    print("Cannot dive by Zero. Enter valid denominator")

except Exception as e:
    print(f"An unexpected error occurred : {e}")