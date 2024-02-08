# 1. Singleton Pattern:
# Explanation: The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.
# This is useful when you want to control the number of instances of a class and ensure that there's only one instance available throughout the application.

# Python Code Example:

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
instance1 = Singleton()
instance2 = Singleton()
print(instance1 is instance2)  # Output: True


# Factory Pattern:
# Explanation: The Factory pattern provides an interface to create objects without exposing the object creation logic to the client.
# It encapsulates object creation within a method or a class, making it easier to manage object instantiation.

# Python Code Example:

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()

# Usage
factory = AnimalFactory()
animal = factory.create_animal("dog")
print(animal.speak())  # Output: Woof!


# Observer Pattern:
# Explanation: The Observer pattern defines a dependency between objects so that when one object (the subject) changes its state,
# all its dependents (observers) are notified and updated automatically.

# Python Code Example:

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received message: {message}")

# Usage
subject = Subject()
observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")

# Strategy Pattern:
# Explanation: The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
# The client code can choose the appropriate algorithm without knowing the details of its implementation.

# Python Code Example:

class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with credit card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal.")

class ShoppingCart:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def checkout(self, amount):
        self._payment_strategy.pay(amount)

# Usage
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

cart1 = ShoppingCart(credit_card_payment)
cart1.checkout(100)  # Output: Paying $100 with credit card.

cart2 = ShoppingCart(paypal_payment)
cart2.checkout(50)  # Output: Paying $50 with PayPal.


# Decorator Pattern:
# Explanation: The Decorator pattern allows behavior to be added to individual objects, either statically or dynamically,
# without affecting the behavior of other objects from the same class. It is used to extend the functionality of objects in a flexible and reusable way.

# Python Code Example:

class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

# Usage
coffee = Coffee()
coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(coffee))

print(coffee_with_milk_and_sugar.cost())  # Output: 8

# Command Pattern:
# Explanation: The Command pattern encapsulates a request as an object, allowing you to parameterize clients with different requests,
# queue or log requests, and support un-doable operations.

# Python Code Example:

class Light:
    def turn_on(self):
        print("Light is on.")

    def turn_off(self):
        print("Light is off.")

class LightOnCommand:
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_on()

class LightOffCommand:
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.turn_off()

class RemoteControl:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def press_button(self):
        self._command.execute()

# Usage
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote_control = RemoteControl()
remote_control.set_command(light_on)
remote_control.press_button()  # Output: Light is on.

remote_control.set_command(light_off)
remote_control.press_button()  # Output: Light is off.

# Adapter Pattern:
# Explanation: The Adapter pattern allows incompatible interfaces to work together. It acts as a bridge between two interfaces, making them work together seamlessly.

# Python Code Example:

class OldPrinter:
    def print_old(self, text):
        print(f"Old Printer: {text}")

class NewPrinter:
    def print_new(self, text):
        print(f"New Printer: {text}")

class PrinterAdapter:
    def __init__(self, new_printer):
        self._new_printer = new_printer

    def print_old(self, text):
        self._new_printer.print_new(text)

# Usage
new_printer = NewPrinter()
adapter = PrinterAdapter(new_printer)
adapter.print_old("Hello World!")  # Output: New Printer: Hello World!


# Template Method Pattern:
# Explanation: The Template Method pattern defines the outline of an algorithm but lets subclasses override specific steps of the algorithm without changing its structure.

# Python Code Example:

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    @abstractmethod
    def step_one(self):
        pass

    @abstractmethod
    def step_two(self):
        pass

    @abstractmethod
    def step_three(self):
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step one.")

    def step_two(self):
        print("Step two.")

    def step_three(self):
        print("Step three.")

# Usage
concrete = ConcreteClass()
concrete.template_method()


# Proxy Pattern:
# Explanation: The Proxy pattern provides a surrogate or placeholder object to control access to another object.
# It can be used to add functionality before or after accessing the original object.

# Python Code Example:

from time import time, sleep

class RealImage:
    def __init__(self, filename):
        self._filename = filename
        self._load_image()

    def display(self):
        print(f"Displaying {self._filename}")

    def _load_image(self):
        sleep(2)
        print(f"Loaded {self._filename}")

class ImageProxy:
    def __init__(self, filename):
        self._filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()

# Usage
image_proxy = ImageProxy("image.jpg")

# RealImage will be loaded only when calling the display method
image_proxy.display()
image_proxy.display()


# Composite Pattern:
# Explanation: The Composite pattern allows you to compose objects into tree-like structures to represent part-whole hierarchies.
# It treats individual objects and compositions of objects uniformly.

# Python Code Example:

class File:
    def __init__(self, name):
        self._name = name

    def display(self, indent=""):
        print(indent + self._name)

class Folder:
    def __init__(self, name):
        self._name = name
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def display(self, indent=""):
        print(indent + "+ " + self._name)
        for child in self._children:
            child.display(indent + "  ")

# Usage
file1 = File("file1.txt")
file2 = File("file2.txt")
folder1 = Folder("Folder 1")
folder1.add(file1)
folder1.add(file2)

file3 = File("file3.txt")
folder2 = Folder("Folder 2")
folder2.add(file3)

root_folder = Folder("Root Folder")
root_folder.add(folder1)
root_folder.add(folder2)

root_folder.display()
