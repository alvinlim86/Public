class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Alvin", 36)
str = "My name is {}. "
str2 = "I am {} this year."
print(str.format(p1.name)+str2.format(p1.age))
