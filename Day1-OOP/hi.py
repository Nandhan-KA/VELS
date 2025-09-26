class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Override the speak method
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):  # Override the speak method
        return f"{self.name} says Meow!"

class Duck(Animal):
    def speak(self):  # Override the speak method
        return f"{self.name} says Quack!"

# Testing method overriding
animals = [
    Animal("Generic Animal"),
    Dog("Buddy"),
    Cat("Whiskers"),
    Duck("Donald")
]

for animal in animals:
    print(animal.speak())