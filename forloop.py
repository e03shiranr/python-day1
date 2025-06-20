A = 1
for A in range(1, 6):
    number = int(input("Please enter the marks: "))
    while number > 100 or number < 0:
        print("Invalid Input")
        number = int(input("Please enter the marks: "))
    if number >= 75:
        print(f"Student {A} got A")
    elif number >= 65 :
        print(f"Student {A} got B")
    elif number >= 50 :
        print(f"Student {A} got C")
    elif number >= 35 :
        print(f"Student {A} got S")
    else:
        print(f"Student {A} failed")
                                                  
 