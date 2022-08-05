#A Class represents a template in which data attributes and methods are layed out. An instance is created when someone uses the template, similar to how a form is considered filled out when a person goes through inputs data.
#Similar to filling out a government form, all boxes must be filled in with appropriate data or "N/A". This requirement is important for designing data strutures since data may not always be present. This problem is solved by using __init__.
#__init__ is used to initialize attributes to solve this problem.
class Dog:
    #The species variable represents a class attribute. A Class attribute is a attribute that has the same value for all class instances. A Class attribute can be recalled the same way as instance attribute.
    species = "Canis familiaris"
    
    #__init__ requires self to be the first argument, however when using the class in a command terminal or creating the class it can be ignored.
    def __init__(self, name, age):
        #self allows attributes to be recalled more easily when using __init__.
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
