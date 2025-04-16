# 🧮 Python Utility Functions

This Python script contains a collection of commonly used utility functions for string manipulation, math operations, conversions, and more. It's great for quick testing, practice, or as a reference while learning Python.

---

## 📚 Included Functions

### 🔤 String Functions

- `reverse_string(s)`  
  Reverses the given string.
  
- `count_vowels(s)`  
  Counts the number of vowels in a string.

---

### 🔢 Number Operations

- `sum_of_digts(num)`  
  Calculates the sum of all digits in a number.

- `sum_natural(n)`  
  Returns the sum of the first `n` natural numbers.

- `sum_e_o(lst)`  
  Returns the sum of even and odd numbers separately from a list.

- `second_largest(lst)`  
  Finds the second largest unique number in a list.

- `factorial_recursion(n)`  
  Returns the factorial using recursion.

---

### 🧮 Math & Conversions

- `decimal_to_binary(n)`  
  Converts a decimal number to binary.

- `binary_to_decimal(n)`  
  Converts a binary string to decimal.

- `circle_area(radius)`  
  Calculates the area of a circle.

- `circumfarance(r)`  
  Calculates the circumference of a circle.

- `lcm(a, b)`  
  Finds the Least Common Multiple (LCM) of two numbers.

- `sqr(a)`  
  Returns the square root of a number.

- `fact(a)`  
  Returns the factorial using the built-in `math.factorial`.

- `fab(n)`  
  Returns the absolute value using `math.fabs`.

- `power(y, x)`  
  Calculates `y` raised to the power of `x`.

---

### 📘 Example Usage

```python
print(reverse_string("Hello"))           # 'olleH'
print(sum_of_digts("12345"))             # 15
print(count_vowels("Hello World"))       # 3
print(sum_natural(5))                    # 15
print(sum_e_o([1, 5, 6, 8, 4]))          # (18, 6)
print(second_largest([1, 3, 5, 6, 8]))   # 6
print(decimal_to_binary(1))              # '1'
print(binary_to_decimal("110010"))       # 50
print(factorial_recursion(0))            # 1
print(circle_area(5))                    # 78.54...
print(lcm(10, 20))                       # 20
print(sqr(25))                           # 5.0
print(fact(5))                           # 120
print(circumfarance(5))                  # 31.41...
print(fab(-10))                          # 10.0
print(power(2, 3))                       # 8.0
