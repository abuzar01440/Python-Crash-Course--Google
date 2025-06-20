# In this code, we will explore Python Type Hints and Type Checking using the typing module.
# We will cover various aspects of type hints, including TypedDict, Union, Optional, Annotated, and more.
# This code is for educational purposes and demonstrates how to use type hints effectively.

# Importing necessary libraries
from typing import List, Dict, Tuple, Set, Callable, Union, Optional
# Importing the typing module for type hints    
print("**"*25, "Python Type Hints and Type Checking","**"*25 )


################################
# Python Type Hints and Type Checking
################################
##################c
print("--"*50)
from typing import TypedDict

class Movie(TypedDict):
    title:str
    year : int

film = Movie(title="avegers infinity war", year=2019)
film_1 = Movie(title="War, Dooms Day", year="2026")
film_2 = Movie(title="War, Dooms Day", year="abuzar shahid")
print(film)
print(film_1)
print(film_2)

##################c
print("--"*50)

from typing import Union

def square(x: Union[int, float]):
    return x * x

x = 3 # or float number
#x= "I am beautiful String" #---> here, it throws an errorrrr

print(square(x))

##################c
print("--"*50)

from typing import Optional
def text(name: Optional[str])->None: # in optional we used one from str, int, float and 2nd would always be None
    if name is None:
        print(f'Hi, How are you random person {name}')
    else:
        print(f'hello Sir, How are you doing {name}')
print("**"*50)
print(text(name="Zar"))
print("**"*50)


print(text(name=None))

#################################################################
print("**"*25, "Annotated","**"*25 )

from typing import Annotated
# it is a type Hint that allows to add metadata to a type.
# it is way to attach additional info such as unit, constraints 
def greet(name: Annotated[str, "The username is ..."])->None:
    print(f"Hello {name}")

print(greet("ALi"))
#############################################
print("**"*25, "Annotated---> Area Calculator","**"*25 )

def area_calculator(length: Annotated[float,"lenght should be positive number"], width: Annotated[float, "Width should be positive"])->None:
    print("The area is ",length * width)

area_calculator(2,3.1)

print("**"*25, "Sequence","**"*25 )

from typing import Sequence

#Sequence of value in a particular data type

def hi_bro(names: Sequence[str]): #it could be list and tuple 
    for name in names:
        print("hello", name)

hi_bro(names=["Ali","Abdullah", "Haider", "Abuzar", "Bhutta"])

##############################################################
# explain other import typing libaries

print("**"*25, "List","**"*25 )
from typing import List
numbers = [1,2,3,4,5]
def sum_of_list(numbers: List[int]) -> int:
    return sum(numbers)

print(sum_of_list(numbers=numbers))

print("**"*25, "Tuple","**"*25 )
from typing import Tuple
def process_coordinates(coordinates: Tuple[float, float]) -> None:
    x, y = coordinates
    print(f"X: {x}, Y: {y}")
process_coordinates(coordinates=(10.5, 20.3))
print("**"*25, "Dict","**"*25 )
from typing import Dict
def get_student_info(student: Dict[str, Union[str, int]]) -> None:
    name = student.get("name")
    age = student.get("age")
    print(f"Student Name: {name}, Age: {age}")
get_student_info(student={"name": "Ali", "age": 20})
print("**"*25, "Set","**"*25 )
from typing import Set
def unique_numbers(numbers: Set[int]) -> None:
    print("Unique Numbers:", numbers)
unique_numbers(numbers={1, 2, 3, 4, 5, 5, 6})
print("**"*25, "Callable","**"*25 )

# Callable is a type hint that indicates that a variable is expected to be a callable object, such as a function or method.
from typing import Callable
def apply_function(func: Callable[[int], int], value: int) -> int:
    return func(value)

# Example of using Callable
def add_one(x: int) -> int:
    return x + 1
result = apply_function(func=add_one, value=10)
print("Result of applying function:", result)

print("**"*25, "Callable with function","**"*25 )

def square(x: int) -> int:
    return x * x

result = apply_function(func=square, value=5)
print("Square of 5 is:", result)


#Difference b/w Dict and TypedDict
print("**"*25, "Difference b/w Dict and TypedDict","**"*25 )
from typing import Dict, TypedDict 
# Dict is a general-purpose dictionary type,
# while TypedDict is a specialized dictionary type that allows you to define the structure of the dictionary with specific keys and their types.
from typing import Dict, Union, TypedDict

# Define a TypedDict for Employee
class Employee(TypedDict):
    name: str
    age: int

def get_employee_info(employee: Dict[str, Union[str, int]]) -> None:
    name = employee.get("name")
    age = employee.get("age")
    print(f"Employee Name: {name}, Age: {age}")

def get_employee_info_typed(employee: Employee) -> None:
    name = employee.get("name")
    age = employee.get("age")
    print(f"Employee Name: {name}, Age: {age}")

employee_info = {"name": "Ali", "age": 30}

# TypedDict is for type hints, not for creating instances — use a dict
employee_info_typed: Employee = {"name": "Ali", "age": 30}

get_employee_info(employee=employee_info)
get_employee_info_typed(employee=employee_info_typed)



##############################################

print("**"*15, "Diff between Dict and TypedDict","**"*15 )

from typing import TypedDict

# ---------- Plain dict ----------
person_dict = {"name": "Ali", "age": 30}  # Any keys, any types allowed

person_dict["address"] = "Pakistan"  # Works fine
person_dict["age"] = "thirty"        # Also allowed — no type check at runtime

print(person_dict)


# ---------- TypedDict ----------
class Person(TypedDict):
    name: str
    age: int

# Correct usage: must match keys & types
person_typed: Person = {"name": "Ali", "age": 30}

# The following would cause a type checker warning:
# person_typed["age"] = "thirty"  # ❌ MyPy/Pyright: type mismatch

print(person_typed)
# Adding a new key not defined in TypedDict
# person_typed["address"] = "Pakistan"  # ❌ MyPy/Pyright: unexpected key
# This would raise a runtime error if you try to access a key that doesn't exist
# person_typed["address"]  # ❌ MyPy/Pyright: key 'address' not found in 'Person'
# TypedDict is more strict about the structure of the dictionary
# and provides better type safety compared to a plain dict.
# It ensures that the keys and their types are defined,
# and any deviation from that structure will raise a type error.
# TypedDict is useful when you want to enforce a specific structure for dictionaries,
# especially when passing data around in your code.
# It helps catch errors early in development by providing type hints.
# In summary, TypedDict is a way to define a dictionary with specific keys and their types,
# while a plain dict is more flexible but less type-safe.

print("**"*15, "Reverse the string","**"*15 )
a= [1,2,3,4,5]
print(list(reversed(a)))
##################################

b= "abuzar"
my_str="".join(reversed(b))
print(my_str)

##################c
print("--"*50)
b = "abuzar"
reverse_0 = b[::-1]
print(reverse_0)
reverse_1 = b[::-2]
print(reverse_1)