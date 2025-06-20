try:
    user_input = input("Enter list of numbers seperated by commas :")
    number_str = user_input.split(',')
    numbers = []

    if not number_str or (len(number_str)== 1 and not number_str[0]):
        raise IndexError("The list is empty.")
    
    for num_str in number_str:
        numbers.append(int(num_str.strip()))

except ValueError:
    print("Error: Non-numeric input encountered. Please enter only numbers")
except IndexError as e:
    print(f"error {e}")
else:
    total_sum = sum(numbers)
    print({total_sum})
finally:
    print("Task Completed !")

    