# **Control Flow Statements**

### Table of Content

- Control Flow 
- if, elif, else Statements
- Nested Conditions
- while Loop
  - else with while
- for Loop
  - Looping over a string
- Nested for Loop
- Enumerate Function in Loops
- range() Function
- Loop Control Statements
  - break
  - continue
  - pass

### **Control Flow**

Control flow allows Python programs to make decisions and repeat actions using conditional statements and loops.

### **if, elif, else Statements**

- **if statement** executes a block of code if the condition is True.
- **elif (else if)** allows checking multiple conditions.
- **else** executes when none of the above conditions are True.
- You can have only **one  else**, but multiple elif blocks.
    
    ```python
    marks = 85
    
    if marks > 90:
        print("Grade: A+")
    elif marks > 80:
        print("Grade: A")  # This block will execute
    elif marks > 70:
        print("Grade: B")
    else:
        print("Grade: C or below")
    ```
    

### **Nested Conditions**

You can place one if or else condition inside another. This is useful for checking multiple levels of logic.

```python
age = 25
country = "India"

if age >= 18:
    if country == "India":
        print("Eligible to vote in India")
    else:
        print("Eligible but not in India")
else:
    print("Not eligible")
```

### **While Loop**

A While loop executes the block as long as the condition is True.

- If the condition never becomes False
- Use break  inside to manually exit if needed

```python
i = 1

while i <= 3:
    print("i is:", i)
    i += 1
```

**Else with While**

- You can use else with while; it runs **after** the loop ends normally (not by Break).
    
    ```python
    i = 1
    
    while i <= 3:
        print(i)
        i += 1
    else:
        print("Loop finished")
    ```
    

### **For Loop**

A for loop is used to iterate over a sequence (string, list, tuple, etc.)

```python
names = ["Dev", "Ashish", "Py"]

for name in names:
    print("Hello", name)
```

**Looping over a string**

```python
for ch in "Python":
    print(ch)
```

**Nested for Loop: can use one ‘for’ inside another**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

### **range() Function**

- **`range()`** is commonly used with **`for`** loops to generate a range of numbers.
    
    ```python
    # range(stop)
    for i in range(5):
        print(i)   # 0 to 4
    
    # range(start, stop)
    for i in range(2, 6):
        print(i)   # 2, 3, 4, 5
    
    # range(start, stop, step)
    for i in range(1, 10, 2):
        print(i)   # 1, 3, 5, 7, 9
    
    # reverse step
    for i in range(10, 0, -2):
        print(i)   # 10, 8, 6, 4, 2
    ```
    
### **Enumerate Function in Loops**

- The `enumerate()` function adds a counter to an iterable. It’s commonly used when you need both the index and value while looping through a list or string.

    ```python
    fruits = ["apple", "banana", "cherry"]

    for index, fruit in enumerate(fruits):
        print(index, fruit)
    ```

    ```python
    #Output
    0 apple
    1 banana
    2 cherry
    ```

- **Example 2: Custom starting index**

    ```python
    fruits = ["mango", "kiwi", "grape"]

    for i, item in enumerate(fruits, start=1):
        print(f"Item {i}: {item}")
    ```

    ```python
    Item 1: mango
    Item 2: kiwi
    Item 3: grape
    ```

### **Loop Control Statements: break, continue, pass**

### Break

- Immediately stops the loop. Used when you want to exit based on a condition.
    
    ```python
    for i in range(1, 6):
        if i == 4:
            break
        print(i)
    ```
    

### Continue

- Skips the current iteration and jumps to the **next cycle** of the loop.
    
    ```python
    for i in range(1, 6):
        if i == 3:
            continue
        print(i)
    ```
    

### Pass

- Does nothing. Used as a **placeholder** for future code or empty control blocks.
    
    ```python
    for i in range(3):
        pass  # Can add login later
    ```
    
    ```python
    if True:
        pass  # placeholder to avoid syntax error
    ```