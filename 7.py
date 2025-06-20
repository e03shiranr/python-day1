try: 
    number = int(input("Please enter the marks: "))
    if number >= 75:
        print("You have A")
    elif number >= 65 :
        print("You have B")
    elif number >= 50 :
        print("You have C")
    elif number >= 35 :
        print("You have S")
    else :
         print("failed")

except ValueError:
    print("Invalid input. Please enter a valid number")