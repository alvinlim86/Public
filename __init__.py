class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):
  pass

p1 = Student("Alvin", 36)
str = "My name is {}. "
str2 = "I am {} this year."
print(str.format(p1.name)+str2.format(p1.age))
