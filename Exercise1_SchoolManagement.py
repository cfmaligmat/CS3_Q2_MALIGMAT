#Exercise1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Viel", 15)

person1.display_info()


print(person1.name)
print(person1.age)

#Exercise2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age 

    def get_Age(self):
        return self.__age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.get_Age()}")


person1 = Person("Viel", 15)

person1.display_info()
print("Accessed via getter:", person1.get_Age())

# Reflection: Why is it better to access __age through get_Age()?
# Accessing __age through a getter method enforces encapsulation and data protection.
# It prevents outside code from accidentally changing or corrupting the value directly,
# and it lets you add validation or formatting logic in one place if your rules change later.

#Exercise3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  
    def get_age(self):
        return self.__age


class Student(Person):
    def study(self):
        print(f"{self.name} is currently studying.")


student1 = Student("Viel", 15)

print("Name:", student1.name)
print("Age:", student1.get_age())

student1.study()


#Exercise4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  

    def get_age(self):
        return self.__age


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is currently teaching.")


teacher1 = Teacher("Sir Xian", 35)

print("Name:", teacher1.name)
print("Age:", teacher1.get_age())

teacher1.teach()

#Exercise5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


class Student(Person):
    def study(self):
        print(f"{self.name} is currently studying.")

    def role(self):
        print(f"{self.name} (Age {self.get_age()}) is a Student who attends classes and learns.")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} is currently teaching.")

    def role(self):
        print(f"{self.name} (Age {self.get_age()}) is a Teacher who prepares lessons and instructs students.")


student1 = Student("Viel", 15)
teacher1 = Teacher("Sir Xian", 35)

student1.role()
teacher1.role()

print("\n--- Comparing in a loop ---")
for person in (student1, teacher1):
    person.role()

#Exercise6
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    @abstractmethod
    def role(self):
        pass


class Student(Person):
    def study(self):
        return f"{self.name} is studying."

    def role(self):
        return f"{self.name} (Age {self.get_age()}): Learns in class"


class Teacher(Person):
    def teach(self):
        return f"{self.name} is teaching."

    def role(self):
        return f"{self.name} (Age {self.get_age()}): Teaches lessons"


try:
    person1 = Person("Lauren", 15)
    person_status = f"{person1.name} (Age {person1.get_age()})"
except TypeError:
    person_status = "Error: Cannot instantiate Person"


student1 = Student("Viel", 15)
teacher1 = Teacher("Sir Xian", 35)


col_width = 36
print(f"{'PERSON (ABSTRACT)':<{col_width}} | {'STUDENT':<{col_width}} | {'TEACHER':<{col_width}}")
print("-" * (col_width * 3 + 6))
print(f"{person_status:<{col_width}} | {student1.role():<{col_width}} | {teacher1.role():<{col_width}}")
print(f"{'No role() implementation':<{col_width}} | {student1.study():<{col_width}} | {teacher1.teach():<{col_width}}")
