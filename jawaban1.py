class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Selamat datang", self.firstname, self.lastname, "dikelas", self.graduationyear)

x = Student("dzaka ", "luthfi", 2023)
x.welcome()
