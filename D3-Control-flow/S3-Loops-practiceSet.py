# 1. write a program to take number from user and then print sum total value from to that n-th number

num = int(input("Enter a number: "))
count = 0
for i in range(1, num+1):
    count += i
print("Sum of 1 to n-th term is: ", count)


# 2. write a program to print multiplication table with user input

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")


# 3. write a program to print reverse count down from a user input 

count = int(input("Enter a number: "))
while count >= 1:
    print(count)
    count -= 1


# 4. write a program to print all the even number between two user input digits

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        print(i)


# 5. write a program to calculate factorial of a number 

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial is: ", fact)
