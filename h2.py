import math
from datetime import datetime
from itertools import groupby
import re
from functools import reduce




def add(a, b):
   while True:
       try:
           return a + b
       except TypeError:
           print("both args gotta be numbers. try again.")
           a = float(input("enter the first number: "))
           b = float(input("enter the second number: "))




def subtract(a, b):
   while True:
       try:
           return a - b
       except TypeError:
           print("both args gotta be numbers. try again.")
           a = float(input("enter the first number: "))
           b = float(input("enter the second number: "))


def multiply(a, b):
   while True:
       try:
           return a * b
       except TypeError:
           print("both args gotta be numbers. try again.")
           a = float(input("enter the first number: "))
           b = float(input("enter the second number: "))


def divide(a, b):
   while True:
       try:
           if b == 0:
               raise ZeroDivisionError("can't divide by zero.")
           return a / b
       except (TypeError, ZeroDivisionError) as e:
           print(f"error: {e}. try again.")
           a = float(input("enter the numerator: "))
           b = float(input("enter the denominator: "))




def cubeminussquare(a, b):
   while True:
       try:
           return a ** 3 - b ** 2
       except TypeError:
           print("both args gotta be numbers. try again.")
           a = float(input("enter the first number: "))
           b = float(input("enter the second number: "))


def squareminuscube(a, b):
   while True:
       try:
           return b ** 3 - a ** 2
       except TypeError:
           print("both args gotta be numbers. try again.")
           a = float(input("enter the first number: "))
           b = float(input("enter the second number: "))


def factorial(n):
   while True:
       try:
           n = int(input("enter a non-negative integer: "))
           if n < 0:
               raise ValueError("can't do factorial of a negative number.")
           return math.factorial(n)
       except ValueError as e:
           print(f"error: {e}. try again.")


def gcd(a, b):
   while True:
       try:
           return math.gcd(a, b)
       except TypeError:
           print("both args gotta be integers. try again.")
           a = int(input("enter the first integer: "))
           b = int(input("enter the second integer: "))


def lcm(a, b):
   while True:
       try:
           if a == 0 or b == 0:
               raise ValueError("can't compute lcm with zero.")
           return abs(a * b) // gcd(a, b)
       except (TypeError, ValueError) as e:
           print(f"error: {e}. try again.")
           a = int(input("enter the first integer: "))
           b = int(input("enter the second integer: "))


def nth_root(x, n):
   while True:
       try:
           if x < 0 and n % 2 == 0:
               raise ValueError("can't compute even root of a negative number.")
           return x ** (1 / n)
       except (TypeError, ValueError) as e:
           print(f"error: {e}. try again.")
           x = float(input("enter the number: "))
           n = int(input("enter the root degree: "))


def sum_of_digits(n):
   while True:
       try:
           return sum(int(digit) for digit in str(n) if digit.isdigit())
       except ValueError:
           print("input must be a non-negative integer. try again.")
           n = int(input("enter a non-negative integer: "))


def is_prime(n):
   while True:
       try:
           if n <= 1:
               return False
           for i in range(2, int(n ** 0.5) + 1):
               if n % i == 0:
                   return False
           return True
       except TypeError:
           print("input must be an integer. try again.")
           n = int(input("enter an integer: "))




def simple_interest(cost_price, rate, time):
   while True:
       try:
           cost_price = float(input("enter the cost price: "))
           rate = float(input("enter the rate of interest: "))
           time = float(input("enter the time period: "))
           return (cost_price * rate * time) / 100
       except ValueError:
           print("invalid input. enter numbers please.")




def celsius_to_fahrenheit(c):
   while True:
       try:
           return (c * 9 / 5) + 32
       except TypeError:
           print("input must be a number. try again.")
           c = float(input("enter the temperature in celsius: "))




def da_calculator(salary):
   while True:
       try:
           salary = float(input("enter the salary: "))
           DA = salary * 0.1
           HRA = salary * 0.05
           MA = salary * 0.1
           PF = 1000
           new_salary = salary + DA + HRA + MA - PF
           return new_salary
       except ValueError:
           print("invalid input. enter a number for salary.")




def print_primes(a, b):
   while True:
       try:
           a = int(input("enter the starting number: "))
           b = int(input("enter the ending number: "))
           if a > b:
               raise ValueError("starting number must be <= ending number.")
           list_of_primes = []
           if a <= 1:
               a = 2


           for n in range(a, b + 1):
               if is_prime(n):
                   list_of_primes.append(n)
                   print(f"{n} is prime")


           return list_of_primes
       except ValueError as ve:
           print(f"invalid input: {ve}. try again.")


def reverse_string(s):
   while True:
       try:
           if not isinstance(s, str):
               raise ValueError("input must be a string.")
           return s[::-1]
       except ValueError as e:
           print(f"error: {e}. try again.")
           s = input("enter a string: ")


def count_vowels(s):
   while True:
       try:
           if not isinstance(s, str):
               raise ValueError("input must be a string.")
           return sum(1 for char in s if char in 'aeiouAEIOU')
       except ValueError as e:
           print(f"error: {e}. try again.")
           s = input("enter a string: ")


def current_datetime():
   return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_age(birthdate):
   while True:
       try:
           today = datetime.today()
           birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
           age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
           return age
       except ValueError:
           print("invalid birthdate format. use YYYY-MM-DD. try again.")
           birthdate = input("enter your birthdate (YYYY-MM-DD): ")




def find_max_min(lst):
   while True:
       try:
           if not lst:
               raise ValueError("list is empty.")
           return max(lst), min(lst)
       except ValueError as e:
           print(f"error: {e}. try again.")
           lst = list(map(int, input("enter a list of numbers separated by spaces: ").split()))


def merge_dicts(dict1, dict2):
   while True:
       try:
           merged_dict = dict1.copy()
           merged_dict.update(dict2)
           return merged_dict
       except AttributeError:
           print("both args gotta be dictionaries. try again.")
           dict1 = eval(input("enter the first dictionary: "))
           dict2 = eval(input("enter the second dictionary: "))


def merge_lists(lst1, lst2):
   return lst1 + lst2


def sort_list(lst):
   while True:
       try:
           return sorted(lst)
       except TypeError:
           print("list must have only comparable elements. try again.")
           lst = list(map(int, input("enter a list of numbers separated by spaces: ").split()))


def average(lst):
   while True:
       try:
           if not lst:
               raise ValueError("list is empty.")
           return sum(lst) / len(lst)
       except (ValueError, TypeError) as e:
           print(f"error: {e}. try again.")
           lst = list(map(int, input("enter a list of numbers separated by spaces: ").split()))


def median(lst):
   while True:
       try:
           if not lst:
               raise ValueError("list is empty.")
           sorted_lst = sorted(lst)
           n = len(sorted_lst)
           if n % 2 == 1:
               return sorted_lst[n // 2]
           else:
               mid1, mid2 = sorted_lst[n // 2 - 1], sorted_lst[n // 2]
               return (mid1 + mid2) / 2
       except (ValueError, TypeError) as e:
           print(f"error: {e}. try again.")
           lst = list(map(int, input("enter a list of numbers separated by spaces: ").split()))


def mode(lst):
   while True:
       try:
           if not lst:
               raise ValueError("list is empty.")
           return max(set(lst), key=lst.count)
       except (ValueError, TypeError) as e:
           print(f"error: {e}. try again.")
           lst = list(map(int, input("enter a list of numbers separated by spaces: ").split()))


def is_anagram(str1, str2):
   while True:
       try:
           if not (isinstance(str1, str) and isinstance(str2, str)):
               raise ValueError("both inputs must be strings.")
           return sorted(str1) == sorted(str2)
       except ValueError as e:
           print(f"error: {e}. try again.")
           str1 = input("enter the first string: ")
           str2 = input("enter the second string: ")


def compress_string(s):
   while True:
       try:
           if not isinstance(s, str):
               raise ValueError("input must be a string.")
           return ''.join(f"{char}{len(list(group))}" for char, group in groupby(s))
       except ValueError as e:
           print(f"error: {e}. try again.")
           s = input("enter a string: ")


def decompress_string(s):
   while True:
       try:
           if not isinstance(s, str):
               raise ValueError("input must be a string.")
           return ''.join(char * int(count) for char, count in re.findall(r'(\D)(\d+)', s))
       except ValueError as e:
           print(f"error: {e}. try again.")
           s = input("enter a compressed string: ")


def generate_multiplication_table(n):
   while True:
       try:
           n = int(n)
           if n <= 0:
               raise ValueError("number must be positive.")
           return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
       except ValueError as e:
           print(f"error: {e}. try again.")
           n = input("enter a positive integer: ")


def is_perfect_number(n):
   while True:
       try:
           if n <= 0:
               raise ValueError("number must be positive.")
           return sum(i for i in range(1, n) if n % i == 0) == n
       except ValueError as e:
           print(f"error: {e}. try again.")
           n = int(input("enter a positive integer: "))


def unique_elements(lst):
   return list(set(lst))


def transpose_matrix(matrix):
   while True:
       try:
           return list(map(list, zip(*matrix)))
       except TypeError:
           print("input must be a list of lists. try again.")
           matrix = eval(input("enter a matrix (list of lists): "))


def gcd_of_list(lst):
   while True:
       try:
           if not lst:
               raise ValueError("list is empty.")
           return reduce(math.gcd, lst)
       except (ValueError, TypeError) as e:
           print(f"error: {e}. try again.")
           lst = list(map(int, input("enter a list of integers separated by spaces: ").split()))


def lcm_of_list(lst):
   while True:
       try:
           def lcm(a, b):
               return abs(a * b) // math.gcd(a, b)
           if not lst:
               raise ValueError("list is empty.")
           return reduce(lcm, lst)
       except (ValueError, TypeError) as e:
           print(f"error: {e}. try again.")
           lst = list(map(int, input("enter a list of integers separated by spaces: ").split()))




def atomicnumber(p, g):
   while True:
       try:
           p = int(p)
           g = int(g)


           if not (1 <= p <= 7):
               raise ValueError("period must be between 1 and 7.")
           if not (1 <= g <= 18):
               raise ValueError("group must be between 1 and 18.")


           if p == 1 and g == 18:
               g = 0
           if p == 1 and g == 1:
               g = -1


           n = p - (math.floor(p / 2) + 1)


           a = (2 * (n * (2 * (n ** 2) + (9 * n) + 13))) // 3 + (2 + g)


           if p % 2 and not (p == 1) == 1:
               a = a - (2 * ((n + 1) ** 2))


           if a > 56:
               a = a + 14


           if p == 2 or p == 3:
               if g >= 13:
                   a -= 10


           if (p == 6 or p == 7) and g == 3:
               while True:
                   try:
                       b = int(input("what is your element's position? "))
                       if b < 1:
                           raise ValueError("position must be positive.")
                       a = a + (b - 1) - 14
                       break
                   except ValueError as ve:
                       print(f"invalid input: {ve}")


           print(f"atomic number result: {a}")
           return a
       except ValueError as ve:
           print(f"error: {ve}. try again.")
           p = input("enter period number: ")
           g = input("enter group number: ")

print(calculate_age("2011-4-22"))