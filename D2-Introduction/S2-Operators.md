# **Operators and Expressions**

**Operators:** are special symbols or keywords used to perform operations on values and variables. An **expression** is a combination of variables, values, and operators that Python interprets and evaluates to produce another value.

### **Arithmetic Operators**

Used for basic mathematical operations.

| Operator | Description          | Example         | Result       |
|----------|----------------------|-----------------|--------------|
| `+`      | Addition              | `x + y`         | Sum          |
| `-`      | Subtraction           | `x - y`         | Difference   |
| `*`      | Multiplication        | `x * y`         | Product      |
| `/`      | Division              | `x / y`         | Quotient (float) |
| `//`     | Floor Division        | `x // y`        | Quotient (floored) |
| `%`      | Modulus               | `x % y`         | Remainder    |
| `**`     | Exponentiation        | `x ** y`        | Power        |

- **Example**

    ```python
    a = 10
    b = 3
    print(a + b)   # Addition: 13
    print(a - b)   # Subtraction: 7
    print(a * b)   # Multiplication: 30
    print(a / b)   # Division: 3.333...
    print(a // b)  # Floor Division: 3
    print(a % b)   # Modulus: 1
    print(a ** b)  # Exponentiation: 1000
    ```

### **Assignment Operators**

Used to assign values to variables, with optional operations.

| Operator | Example      | Same As           |
|----------|--------------|-------------------|
| `=`      | `x = 5`      | x = 5             |
| `+=`     | `x += 3`     | x = x + 3         |
| `-=`     | `x -= 2`     | x = x - 2         |
| `*=`     | `x *= 4`     | x = x * 4         |
| `/=`     | `x /= 2`     | x = x / 2         |
| `//=`    | `x //= 2`    | x = x // 2        |
| `%=`     | `x %= 3`     | x = x % 3         |
| `**=`    | `x **= 2`    | x = x ** 2        |

- **Example**
    
    ```python
    x = 10
    x += 5    # x becomes 15
    x *= 2    # x becomes 30
    ```

### **Comparison Operators**

Compare values and return a boolean result (`True` or `False`).

| Operator | Description         | Example     |
|----------|---------------------|-------------|
| `==`     | Equal to            | `x == y`    |
| `!=`     | Not equal to        | `x != y`    |
| `>`      | Greater than        | `x > y`     |
| `<`      | Less than           | `x < y`     |
| `>=`     | Greater or equal to | `x >= y`    |
| `<=`     | Less or equal to    | `x <= y`    |

- **Example**
    
    ```python
    a = 7
    b = 5
    print(a == b)       # False
    print(a != b)       # True
    print(a > b)        # True
    print(a <= b)       # False
    ```

### **Logical Operators (`and`, `or`, `not`)**

Used to combine conditional statements.

| Operator | Description                   | Example                |
|----------|-------------------------------|------------------------|
| `and`    | True if both conditions true  | `x > 5 and x < 10`     |
| `or`     | True if at least one is true  | `x > 5 or x < 3`       |
| `not`    | Inverts the boolean result    | `not(x > 5)`           |

- **Example**
    
    ```python
    x = 8
    print(x > 5 and x < 10)     # True
    print(x > 10 or x == 8)     # True
    print(not(x == 8))          # False
    ```

### **Bitwise Operators**

Operate on binary representations of numbers.

| Operator | Description       | Example     |
|----------|-------------------|-------------|
| `&`      | Bitwise AND       | `x & y`     |
| `|`      | Bitwise OR        | `x | y`     |
| `^`      | Bitwise XOR       | `x ^ y`     |
| `~`      | Bitwise NOT       | `~x`        |
| `<<`     | Left Shift        | `x << 2`    |
| `>>`     | Right Shift       | `x >> 2`    |

- **Example**
    
    ```python
    x = 5 # Binary: 0b0101
    y = 3 # Binary: 0b0011

    print(x & y)            #Output 1
    print(x | y)            #Output 7
    print(x ^ y)            #Output 6
    print(~x)               #Output -6
    print(x << 1)           #Output 10
    print(x >> 1)           #Output 2
    ```

### **Identity and Membership Operators**

Used to test object identity and membership in sequences.


#### Identity Operators

| Operator | Description               | Example     |
|----------|---------------------------|-------------|
| `is`     | True if same object       | `x is y`    |
| `is not` | True if not same object   | `x is not y`|

- **Example**
    
    ```python
    a = [1, 2]
    b = a
    c = [1, 2]

    print(a is b)     # True  (same object)
    print(a is c)     # False (different objects)
    print(a == c)     # True (values are equal)
    ```

#### Membership Operators

| Operator  | Description          | Example            |
|-----------|----------------------|--------------------|
| `in`      | True if value exists | `"a" in "cat"`     |
| `not in`  | True if not exists   | `"x" not in "cat"` |

- **Example**
    
    ```python
    numbers = [1, 2, 3, 5]

    print(2 in numbers)       # True
    print(4 not in numbers)   # True
    ```

### **Operator Precedence and Associativity**

#### Operator Precedence

Determines the order in which operations are evaluated.

**From highest to lowest:**

1. Parentheses `()`
2. Exponentiation `**`
3. Unary Operators `+`, `-`, `~`
4. Multiplication, Division, Floor Div, Modulus `*`, `/`, `//`, `%`
5. Addition and Subtraction `+`, `-`
6. Bitwise Shift `<<`, `>>`
7. Bitwise AND `&`
8. Bitwise XOR `^`
9. Bitwise OR `|`
10. Comparison Operators (`==`, `!=`, `>`, `<`, etc.)
11. `not`
12. `and`
13. `or`
14. Assignment Operators (`=`, `+=`, etc.)
15. Identity and Membership (`is`, `in`, `not in`, etc.)

- **Example**
    
    ```python
    result = 2 + 3 * 4 # 14 → 3*4=12, then 2+12
    result2 = (2 + 3) * 4 # 20 → Parentheses change order
    ```

#### Associativity

- **Left to Right** → Most operators (`+`, `-`, `*`, etc.)
- **Right to Left** → `=`, `**`, etc.

    
    ```python
    result = 2 + 3 * 4 # 14 → 3*4=12, then 2+12
    result2 = (2 + 3) * 4 # 20 → Parentheses change order
    ```