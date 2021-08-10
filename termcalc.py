import math

print("Store 2 number to begin")

a = int(input("First Number: "))
b = int(input("Second Number: "))

print("""
    Choose your calculation:
    1, Addition
    2. Multiplication
    3. Division
    4. Substraction
""")

userpick = int(input("Type 1, 2, 3 or 4 here then press enter: "))

def calculation():
    sum = a + b
    multiply = a * b
    dev = a / b
    subtract = a - b

    if userpick == 1:
        print("Your answer to that is: " + str(sum))
    elif userpick == 2:
        print("Your answer to that is: " + str(multiply))
    elif userpick == 3:
        print("Your answer to that is: " + str(dev))
    elif userpick == 4:
        print("Your answer to that is: " + str(subtract))
    else:
        return None

calculation()


