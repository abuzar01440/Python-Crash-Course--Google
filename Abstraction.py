# what is Abstraction in Python OOPs
# Abstraction is a process of hiding the implementation details and showing only functionality to the user.
# It helps to reduce complexity and increase efficiency.
# Abstraction can be achieved through abstract classes and interfaces.
# Abstract classes are classes that cannot be instantiated and can contain abstract methods (methods without implementation).
# Interfaces are a way to achieve abstraction in Python. 
#                      They are a set of methods that must be implemented by any class that inherits from the interface.

# In Python, we can achieve abstraction using the abc module (Abstract Base Classes).
# The abc module provides the ABC class and the abstractmethod decorator to define abstract classes and methods.
# The ABC class is a base class for defining abstract classes, and the abstractmethod decorator is used to define abstract methods.
# Abstract classes can have both abstract and concrete methods (methods with implementation).
# Abstract methods must be implemented by any subclass of the abstract class.
# Concrete methods can be used as is or overridden by subclasses.
# Abstract classes can also have attributes and properties.
# Abstract classes can be used to define a common interface for a group of related classes.
# This allows us to create a hierarchy of classes that share common functionality and behavior.
# Abstract classes can also be used to define a common interface for a group of related classes.

# what is the difference between abstraction and encapsulation in Python OOPs
# Abstraction is the process of hiding the implementation details and showing only functionality to the user.
# Encapsulation is the process of wrapping data and methods into a single unit (class) and restricting access to the inner workings of that class.
# Encapsulation is achieved through access modifiers (public, private, protected) and properties.
# Access modifiers are used to restrict access to the attributes and methods of a class.
# Public attributes and methods can be accessed from outside the class, while private attributes and methods cannot be accessed from outside the class.
# Protected attributes and methods can be accessed from within the class and its subclasses.
# Properties are used to define getter and setter methods for attributes, allowing us to control access to the attributes of a class.
# Properties can be used to define read-only or write-only attributes, or to perform validation on attribute values.

# What is interface in Python OOPs
# An interface is a way to achieve abstraction in Python.
# Explain An interface is a way to achieve abstraction in Python.
# An interface is a set of methods that must be implemented by any class that inherits from the interface.
# Interfaces are used to define a common interface for a group of related classes.

# Abstraction

class Emailservice:
    def _connect(self):
        print("Connecting to email server...")
        # code to connect to email server
        print("Connected to email server.")
    def _authenticate(self):
        print("Authenticating user...")
        # code to authenticate user
        print("User authenticated.")
    def send_email(self, email):
        self._connect()                          # This is a private method
        self._authenticate()    # This is a private method
        print(f"Sending email to {email}...")
        # code to send email
        print("Email sent.")

    def disconnect(self):
        print("Disconnecting from email server...")
        # code to disconnect from email server
        print("Disconnected from email server.")


emailservice = Emailservice()
print(emailservice.send_email(email='zac@gmail.com'))
print(emailservice.disconnect())
print(emailservice._connect()) # This is not recommended as it is a private method
print(emailservice._authenticate()) # This is not recommended as it is a private method

# The above code is an example of abstraction in Python.
# The Emailservice class has a public method send_email() that is used to send an email.
# The send_email() method calls the private methods _connect() and _authenticate() to connect to the email server and authenticate the user.
# The _connect() and _authenticate() methods are not intended to be called from outside the class, as they are private methods.
# if we don't make protected methods, we can call them from outside the class, but it is not recommended as it is a private method.
# the protected methods are intend to reduce the complexity of the code and increase efficiency.

#######################################################################################################


""""What is Abstraction?

At its core, abstraction is about hiding complexity and showing only essential features.
 Think about driving a car: you use the steering wheel, pedals, and gear stick (the interface),
   but you don't need to know the intricate details of the engine, transmission,
     or combustion process (the implementation) to drive it."""

""""Even without special tools, basic Python classes inherently provide a level of abstraction.
 When you create a class and its methods, users of that class interact with the methods without
   needing to know exactly how each method achieves its result internally."""


# Simple example: A basic calculator

class SimpleCalculator:
    def add(self, x, y):
        # The internal detail (direct addition) is hidden from the user
        # who just calls .add()
        result = x + y
        # Maybe there's complex logging or validation here in a real app
        # print(f"Performing addition: {x} + {y}")
        return result

    def subtract(self, x, y):
        # Internal detail
        result = x - y
        # print(f"Performing subtraction: {x} - {y}")
        return result

# --- User Interaction ---
calc = SimpleCalculator()
sum_result = calc.add(10, 5)       # User calls add, gets result
diff_result = calc.subtract(10, 5) # User calls subtract, gets result

print(f"Sum: {sum_result}")         # Output: Sum: 15
print(f"Difference: {diff_result}") # Output: Difference: 5

# The user doesn't need to know *how* add or subtract work inside the class.
# They just know the 'interface' (the methods available and what they do).


""""Formal Abstraction with abc Module

Python provides the abc (Abstract Base Classes) module to define formal abstract classes and methods.
 This is often used when designing frameworks or ensuring that subclasses adhere to a specific structure or "contract".

Abstract Base Class (ABC): A class that cannot be instantiated directly. It's meant to be subclassed.
 You define one by inheriting from abc.ABC.
Abstract Method: A method declared in an ABC (using the @abc.abstractmethod decorator)
 but without an implementation. Subclasses must implement this method to be instantiable."""


import abc

# Define an Abstract Base Class 'Shape'
class Shape(abc.ABC):

    @abc.abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass # No implementation here

    @abc.abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass # No implementation here

    def describe(self):
        # A regular method can also exist in an ABC
        print(f"This is a shape.")

# --- Subclasses implementing the abstract methods ---

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        # Mandatory implementation
        return self.width * self.height

    def perimeter(self):
        # Mandatory implementation
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        pi = 3.14159 # Approximation

    def area(self):
        # Mandatory implementation
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        # Mandatory implementation (circumference)
        return 2 * 3.14159 * self.radius

# --- Usage ---

# try:
#     # This will fail because Shape has abstract methods
#     generic_shape = Shape()
# except TypeError as e:
#     print(f"Error: {e}") # Output: Error: Can't instantiate abstract class Shape with abstract methods area, perimeter

rect = Rectangle(10, 5)
circ = Circle(7)

shapes = [rect, circ]

for shape in shapes:
    shape.describe() # Calling the non-abstract method from base class
    # Polymorphism in action: calling the same method name,
    # but getting the specific implementation for each object type.
    print(f"Type: {type(shape).__name__}, Area: {shape.area()}, Perimeter: {shape.perimeter()}")

# Output:
# Error: Can't instantiate abstract class Shape with abstract methods area, perimeter
# This is a shape.
# Type: Rectangle, Area: 50, Perimeter: 30
# This is a shape.
# Type: Circle, Area: 153.93791, Perimeter: 43.98226