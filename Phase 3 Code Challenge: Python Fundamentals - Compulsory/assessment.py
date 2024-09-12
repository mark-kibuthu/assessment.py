# def add_numbers(num1, num2):
#     return num1 + num2

# def is_even(number):
#     return number % 2 == 0

# def reverse_string(text):
#     return text[::-1]

# def count_vowels(text):
#     vowels = 'aeiou'
#     count = 0
#     for char in text.lower():
#         if char in vowels:
#             count += 1
#     return count

# def calculate_factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     factorial = 1
#     for i in range(2, n + 1):
#         factorial *= i
#     return factorial

# def decorator_func(func):
#     def wrapper(*args, **kwargs):
#         print("Decorator Applied")
#         return func(*args, **kwargs)
#     return wrapper

# def apply_decorator(func):
#     return decorator_func(func)

# def sort_by_age(people):
#     return sorted(people, key=lambda person: person[1])

# def merge_dicts(dict1, dict2):
#     merged = dict1.copy()
#     for key, value in dict2.items():
#         if key in merged:
#             merged[key] += value
#         else:
#             merged[key] = value
#     return merged

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"Car Information: {self.year} {self.make} {self.model}")
