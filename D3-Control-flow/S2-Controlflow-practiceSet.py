# 1. Write program to take user input & check whether the number is Even or Odd.


val = int(input("Enter a Number: "))
if val % 2 == 0:
    print(val, "is an Even Number")
else:
    print(val, "is an Odd Number")


# 2. write a program to check whether the number is psoitive, negative or zero.


num = int(input("Enter a Number: "))
if num < 0:
    print(f"{num} is a Negative Number")
elif num == 0:
    print("This value is Zero")
else:
    print(f"{num} is a Positive Number")


# 3. write a program to take 3 user inputs and print the largest one


a, b, c = map(int, input("Enter a Number: ").split())
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


# 4. write a program to pass traffic light messages according to the color given by user


color = input("Enter traffic light color (red/yellow/green): ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")

