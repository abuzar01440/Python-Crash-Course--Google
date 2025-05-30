# 🐍 Python Crash Course - Google 🐍
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Concepts-brightgreen?style=for-the-badge)
![Course](https://img.shields.io/badge/Course-Week_4-blue?style=for-the-badge)

<div align="center">
  
  ```
   ____        _   _                   ____                _      ____                          
  |  _ \ _   _| |_| |__   ___  _ __   / ___|_ __ __ _ ___| |__  / ___|___  _   _ _ __ ___  ___ 
  | |_) | | | | __| '_ \ / _ \| '_ \ | |   | '__/ _` / __| '_ \| |   / _ \| | | | '__/ __|/ _ \
  |  __/| |_| | |_| | | | (_) | | | || |___| | | (_| \__ \ | | | |__| (_) | |_| | |  \__ \  __/
  |_|    \__, |\__|_| |_|\___/|_| |_| \____|_|  \__,_|___/_| |_|\____\___/ \__,_|_|  |___/\___|
         |___/                                                                                  
  ```
  
</div>

## 📋 Table of Contents
- [🌟 Overview](#-overview)
- [🎯 Key Topics](#-key-topics)
- [📁 Repository Structure](#-repository-structure)
- [🧩 OOP Concepts Explained](#-oop-concepts-explained)
- [🚀 Getting Started](#-getting-started)
- [📝 Examples](#-examples)
- [🔍 Resources](#-resources)

## 🌟 Overview
This repository contains materials from Week 4 of the Python Crash Course by Google, focusing on Object-Oriented Programming (OOP) concepts in Python. The repository includes practical examples and explanations of core OOP principles like classes, objects, inheritance, encapsulation, and abstraction.

## 🎯 Key Topics
- 📦 **Classes and Objects**
- 🔒 **Encapsulation**
- 🎭 **Abstraction**
- 🧬 **Inheritance**
- 🦆 **Duck Typing**
- 📊 **Static Attributes**

## 📁 Repository Structure
```
Python-Crash-Course--Google/
├── Abstraction.py           # Demonstrates abstraction concepts
├── Encapsulation.py         # Examples of encapsulation techniques
├── Static Attribute.py      # Working with static/class attributes
├── class cat.py             # Basic class implementation example
├── hasattr.py               # Using hasattr for duck typing
└── info.py                  # Variable scope and access modifiers
```

## 🧩 OOP Concepts Explained

### 🏗️ Classes and Objects
The foundation of OOP in Python. Classes are blueprints, and objects are instances of these blueprints.

```python
# Example from class cat.py
class Cat:
    def __init__(self, name:str, breed:str, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f"The {self.name} cat breed is {self.breed} and its owner detail is {self.owner}")
```

### 🔒 Encapsulation
Encapsulation is the concept of bundling data and methods that work on that data within one unit and restricting access to some of the object's components.

- 🟢 **Public** attributes: `self.variable`
- 🟡 **Protected** attributes: `self._variable` (convention only)
- 🔴 **Private** attributes: `self.__variable` (name mangling applied)

```python
# Example from Encapsulation.py
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # Public attribute
        self._account_type = "Savings"  # Protected attribute
        self.__balance = balance  # Private attribute
```

### 🎭 Abstraction
Abstraction focuses on hiding complex implementation details and showing only the essential features of an object.

```python
# Example from Abstraction.py
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass
```

### 📊 Static Attributes
Static attributes (also called class attributes) are shared across all instances of a class.

```python
# Example from Static Attribute.py
class User:
    count_user = 0  # Static attribute
    def __init__(self, username:str, email:str): 
        self.username = username
        self.email = email
        User.count_user += 1
```

### 🦆 Duck Typing
Duck typing is a concept where the type or class of an object is less important than the methods it defines or the attributes it has.

```python
# Example from hasattr.py
def make_it_walk_and_quack(animal):
    if hasattr(animal, 'walk') and hasattr(animal, 'quack'):
        print(f"It walks: {animal.walk()}")
        print(f"It quacks: {animal.quack()}")
    else:
        print("This object cannot walk and quack like a duck.")
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Basic understanding of Python syntax

### Running the Examples
1. Clone the repository:
   ```bash
   git clone https://github.com/abuzar01440/Python-Crash-Course--Google.git
   ```
2. Navigate to the repository folder:
   ```bash
   cd Python-Crash-Course--Google
   ```
3. Run any example file:
   ```bash
   python "class cat.py"
   ```

## 📝 Examples

### Creating and Using Classes
```python
# From class cat.py
owner_1 = Owner("Saif", "lahore", 92323456789)
cat_1 = Cat(name="oscar", breed="persian", owner=owner_1)
print(cat_1.breed)  # Outputs: persian
print(cat_1.owner.name)  # Outputs: Saif
```

### Implementing Abstraction
```python
# From Abstraction.py
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

### Working with Encapsulation
```python
# From Encapsulation.py
portfolio = StockPortfolio("John Doe")
portfolio.buy_stock("AAPL", 10, 150)
portfolio.buy_stock("MSFT", 5, 200)
print(portfolio.get_portfolio_summary())
```

## 🔍 Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python OOP Tutorial](https://realpython.com/python3-object-oriented-programming/)

---

<div align="center">
  <p>
    <a href="https://github.com/abuzar01440">
      <img src="https://img.shields.io/github/followers/abuzar01440?label=Follow&style=social" alt="GitHub Follow">
    </a>
    ⭐ Star this repository if you found it helpful! ⭐
  </p>
  
  <p>📧 Contact: abuzar01440</p>
  
  <p>Happy Coding! 💻</p>
</div>
