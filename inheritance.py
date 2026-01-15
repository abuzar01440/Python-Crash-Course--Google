
# inheritance in python OOPs
# single inheritance: when a child class inherits from a single parent class
class Parent:
    def func1(self):
        print("this function is in parent class")
        
class Child(Parent):
    def func2(self):
        print("this function is in child class")
        
object = Child()
object.func1()
object.func2()

# multi-level inheritance: when a child class inherits from a parent class, and another child class inherits from that child class
class Parent:
    def func1(self):
        print("this function is in parent class")
        
class Child(Parent):
    def func2(self):
        print("this function is in child class")
        
class GrandChild(Child):
    def func3(self):
        print("this function is in grandchild class")
        
object = GrandChild()
object.func1()
object.func2()
object.func3()

print("\n")
print("=="* 20)
print("multiple inheritance example below:\n")
# multiple inheritance: when a child class inherits from multiple parent classes
class Parent1:
    def func1(self):
        print("this function is in parent class 1")
        
class Parent2:
    def func2(self):
        print("this function is in parent class 2")
        
class Child(Parent1, Parent2):
    def func3(self):
        print("this function is in child class")
        
object = Child()
object.func1()
object.func2()
object.func3()

print("\n")
print("=="* 20)
print("hybrid inheritance example below:\n")
# hybrid inheritance: a combination of two or more types of inheritance
class Parent:
    def func1(self):
        print("this function is in parent class")
        
class Child1(Parent):
    def func2(self):
        print("this function is in child class 1")
        
class Child2(Parent):
    def func3(self):
        print("this function is in child class 2")

class GrandChild(Child1, Child2):
    def func4(self):
        print("this function is in grandchild class")

object = GrandChild()
object.func1()
object.func2()
object.func3()
object.func4()

print("\n")
print("=="* 20)
print("hierarchical inheritance example below:\n")
# hierarchical inheritance: when multiple child classes inherit from a single parent class
class Parent:
    def func1(self):
        print("this function is in parent class")

class Child1(Parent):
    def func2(self):
        print("this function is in child class 1")

class Child2(Parent):
    def func3(self):
        print("this function is in child class 2")

object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()

object2.func1()
object2.func3()

print("\n")
print("=="* 20)
print("demonstration of method resolution order (MRO) in multiple inheritance below:\n")
# method resolution order (MRO) in multiple inheritance
class Parent1:
    def func1(self):
        print("this function is in parent class 1")
        
class Parent2:
    def func1(self):
        print("this function is in parent class 2")
        
class Child(Parent1, Parent2):
    def func2(self):
        print("this function is in child class")
        
object = Child()
object.func1()

print("\n")
print("=="* 20)
print("demonstration of super() function in inheritance below:\n")
# super() function in inheritance
class Parent:
    def __init__(self, parent_attribute):
        self.parent_attribute = parent_attribute
        print("Parent class constructor called")

    def parent_method(self):
        print("Parent class method called")
        print("Parent attribute:", self.parent_attribute)

class Child(Parent):
    def __init__(self, child_attribute):
        super().__init__("Parent attribute value")
        self.child_attribute = child_attribute
        print("Child class constructor called")

    def child_method(self):
        print("Child class method called")
        print("Child attribute:", self.child_attribute)
        super().parent_method()

child_object = Child("Child attribute value")
child_object.child_method()
# This code demonstrates various types of inheritance in Python OOPs including single, multi-level, multiple, hybrid, and hierarchical inheritance.
# It also illustrates method resolution order (MRO) in multiple inheritance and the use of the super() function to access parent class methods and constructors.
# Various types of inheritance in Python OOPs
# Inheritance
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class). This promotes code reusability and establishes a hierarchical relationship between classes.
# Types of Inheritance
# Single Inheritance
# Multi-level Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Hierarchical Inheritance
# Method Resolution Order (MRO)
# super() Function
