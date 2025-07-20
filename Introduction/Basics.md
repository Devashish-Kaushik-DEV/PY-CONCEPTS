# **Python Introduction & Basics**

### Table of Content

- Variables in Python
- Type Casting Variables
- Scope of Variable
- Input and Output in python

**Founder: Python was created by Guido van Rossum in 1991**

### **Python Key Features**

1. Interpreted Language: no need for compilation, executed line by line.
2. Dynamically Typed: no need to declare variable types
3. High-Level Language: Abstracts away memory management and low-level operations.
4. Object-Oriented & Functional: supports OOPs and functional programming.
5. Community Support: large active community and resources.

### Variables in Python

- **Definition:** A variable in Python is a named reference used to store and manage data values in a program (A container for a value). python is dynamically typed language so do not require explicit type declaration.
    
    ```python
    name = “Devashish”
    print(name)
    
    age =  20 
    ```
    

### Rules for naming Variables

- Variable names can only contain letters, digits and underscores.
- A variable name cannot start with a digit.
- Variable names are case-sensitive. (Name and name are not same)
- Avoid using Keywords as variable names. (e.g. true, false, if, else)

    ```python
    # Valid Variables
    name = “Dev”
    _age = 20
    User_Name = "Devashish"
    ```

    ```python
    # Invalid Variables
    1name = "wrong"
    class = 20
    user/name = "Dev"
    ```

### **Variable Assignment**

- **Definition: Variable assignment is the process of giving a value to a variable.**
    
    ```python
    name = "Devashish"   # Basic assignment
    x = "user"
    x = "USER"     # Dynamic Typing assignment
    a = b = c = 100
    print(a,b,c)     # Multiple assignment
    x, y, z = "name", 12, 200.2
    print(x,y,z)
    ```
    

### **Type Casting Variables**

- **Definition: Type casting refers to the process of converting the value of one data type into another. python offers many built-in functions for type casting, as int(), float(), str() etc.**
    
    ```python
    d = "69"
    a = int(d) # Cast string into integer value
    abc = 69
    flt = float(abc) # Cast integer into float value
    x = 69
    new_x = str(x) # Cast integer to string value
    
    # Getting Variable type 
    example = "hello world"
    print(type(example))  #output: String
    ```
    

### **Scope of Variable**

**There are two methods how we define scope of a variable. (global / local)**

### Local Scope

- **Definition: A local scope variable is a variable that is defined within a function or block and can only be accessed and used within that same function or block.**
    
    ```python
    def func():
        a = "I am local Scope"
        print(a)
    print(a)  # will throw error
    ```
    

### Global Scope

- **Definition: A Global scope variable refers to variables that are declared outside of any function or block and can be accessed from anywhere in the code, including inside functions.**
    
    ```python
    a = "I am global Scope"
    
    def func():
        print(a)
    func()      #output: I am global Scope
    print(a)    #output: I am global Scope
    ```
    

### Input and Output in python (I/O)

Print function: Print( ) is used to display the output of computation.

Input function: Input( ) is used to take user input for the computation.

```python
name = input("Enter user name: ")
print(f"Hello {name}, welcome!")
```

**Taking Multiple Inputs**

```python
user1, user2, user3 = input("Enter three User names: ").split()
print("First user name : ", user1)
print("Second user name : ", user2)
print("Third user name : ", user3)
```

**Typecasted Inputs**

```python
a = int(input("Enter a number: "))
print(a)    # Typecasting to integer

b = float(input("Enter a decimal number: "))
print(b)    #Typecasting to float

c = str(input("Enter a string value: "))
print(c)    #Typecasting to string
```

**Output Formatting**

1. Using f-string 
    
    ```python
    name = "Devashish
    age = 20
    print(f"My name is {name} and I am {age} years old.")
    ```
    
2. Using str.format()
    
    ```python
    name = "Devashish"
    age = 20
    print("My name is {} and I am {} years old.".format(name, age))
    ```
    
3. Formatting numbers
    
    ```python
    pi = 3.14159
    print(f"Value of pi: {pi:.2f}")  #turned into 2 decimal
    # Output: Value of pi: 3.14
    ```
    
4. Multi-line Formatting
    
    ```python
    name = "Dev"
    marks = 93.456
    print(f"""
    Report Card
    -----------
    Name: {name}
    Score: {marks:.1f}
    """)
    ```