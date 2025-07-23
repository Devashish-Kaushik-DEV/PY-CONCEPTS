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


# 5. write a program to take password input from user and tell whether the password strength is weak, medium, strong based on length of characters

password = input("Enter your password: ")
length = len(password)
if length <= 4:
    print("Weak password")
elif length <= 7:
    print("Medium Strength password")
else:
    print("Strong password")


# 6. Write a program for Rock, paper, Scissors game, take two player choices and prints who wins.

player1 = input("Player 1 (rock/paper/scissors): ").lower()
player2 = input("Player 2 (rock/paper/scissors): ").lower()

if player1 == player2:
    print("Tie!!")
elif (player1 == "rock" and player2 == "paper") or \
     (player1 == "paper" and player2 == "scissors") or \
     (player1 == "scissors" and player2 == "rock"):
    print("Player 2 wins")
else:
    print("Player 1 wins")


# 7. write a program for a login authentication message. take input from user such as username and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Devashish" and password == "pass12":
    print("Logged in Successfully")
elif username != "Devashish" and password != "pass12":
    print("Invalid username and password")
elif username != "Devashish":
    print("Invalid username!")
else:
    print("Invalid password!")