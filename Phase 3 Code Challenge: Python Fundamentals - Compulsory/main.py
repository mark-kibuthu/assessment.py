# main.py
from add_numbers import add_numbers
from is_even import is_even
from reverse_string import reverse_string
from count_vowels import count_vowels
from calculate_factorial import calculate_factorial
from decorator_func import apply_decorator
from sort_by_age import sort_by_age
from merge_dicts import merge_dicts
from car import Car

# Test add_numbers
print(add_numbers(10, 5))

# Test is_even
print(is_even(4))

# Test reverse_string
print(reverse_string("hello"))

# Test count_vowels
print(count_vowels("helloIO"))

# Test calculate_factorial
print(calculate_factorial(5))

# Test decorator
@apply_decorator
def test_func():
    return "Hello World"
print(test_func())

# Test sort_by_age
people = [("John", 30), ("Jane", 25), ("Dave", 35)]
print(sort_by_age(people))

# Test merge_dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2))

# Test Car class
my_car = Car("Toyota", "Vitz", 2020)
my_car.display_info()
