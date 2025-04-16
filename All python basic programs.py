def reverse_string(s):
   return s[::-1]
   print(reverse_string("Hello"))
 
'''sum of digits'''
def sum_of_digts(num):
    return sum(int(digit)for digit in str(num))
print(sum_of_digts("12345"))

def count_vowels(s):
    return sum(1 for c in s if c.lower() in 'aeiou')
print(count_vowels("Hello World"))

def sum_natural(n):
    return n*(n+1)//2
print(sum_natural(5))

def muti(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
# muti(5)

def sum_e_o(lst):
    even_sum=sum(x for x in lst if x%2==0)
    odd_sum=sum(x for x in lst if x%2!=0)
    return even_sum,odd_sum
print(sum_e_o([1,5,6,8,4]))

def second_largest(lst):
    return sorted(set(lst))[-1]
print(second_largest([1,3,5,6,8]))

def decimal_to_binary(n):
    return bin(n)[2:]
print(decimal_to_binary(1))

def binary_to_decimal(n):
    return int(n,2)
print(binary_to_decimal("110010"))

def factorial_recursion(n):
    return 1 if n==0 else n*factorial_recursion(n-1)
print(factorial_recursion(0))

import math

def circle_area(radius):
    return math.pi*radius**2
print(circle_area(5))

def lcm(a,b):
    from math import gcd 
    return abs(a*b)//gcd(a,b)
print(lcm(10,20))

def sqr(a):
    from math import sqrt
    return sqrt(a)
print(sqr(25))

def fact(a):
    from math import factorial
    return factorial(a)
print(fact(5))

def circumfarance(r):
    return math.pi*2*r
print(circumfarance(5))

def fab(n):
    from math import fabs
    return fabs(n)
print(fab(-10))

def power(y,x):
    from math import pow
    return pow(y,x)
print(power(2,3))
