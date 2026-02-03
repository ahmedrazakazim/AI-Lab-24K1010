class Student_result_system:
  def __init__(self, name, roll_no, marks):
    self.name = name
    self.roll_no = roll_no
    self.__marks = marks

  def set_marks(self, marks):
    self.__marks = marks

  def get_marks(self):
    return self.__marks

  def calculate_grade(self):
    marks = self.get_marks()
    if marks >= 90:
      return 'A'
    elif marks >= 80:
      return 'B'
    elif marks >= 70:
      return 'C'
    elif marks >= 60:
      return 'D'
    else:
      return 'F'
  
  def display(self):
    print(f"Name: {self.name}")
    print(f"Roll No: {self.roll_no}")
    print(f"Marks: {self.__marks}")
    print(f"Grade: {self.calculate_grade()}\n")


s1 = Student_result_system('Ahmed', 1010, 95)
s2 = Student_result_system('Ali', 1004, 85)

s1.display()
s2.display()

s1.set_marks(89)
s2.set_marks(79)

s1.display()
s2.display()
