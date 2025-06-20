class NegativeNumberError(ValueError):
    def returnerror(ValueError):
        print(ValueError)
    

def get_positive_number():
    while True:
        try:
            num_str = input("Please neter a positive number :")
            number = float(num_str)

            if number < 0:
                raise NegativeNumberError("Number must be positive.")
            return number
        except NegativeNumberError as e:
            print(f"Error {e}")

if __name__ == "__main__":
    try:
        positive_num = get_positive_number()
        print(f"You entered a positive number: {positive_num}")
    except NegativeNumberError as e:
        print(f"Caught and error in the main scirpt: {e}")
    except Exception as e:
        print(f"unexpected eroor occured: {e}")
        
